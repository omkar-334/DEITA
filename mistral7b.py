import os

from modal import Image, Secret, Stub, method

MODEL_DIR = "/model"
BASE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"


def download_model_to_folder():
    from huggingface_hub import snapshot_download
    from transformers.utils import move_cache

    os.makedirs(MODEL_DIR, exist_ok=True)

    snapshot_download(
        BASE_MODEL,
        local_dir=MODEL_DIR,
        token=os.environ["HF_TOKEN"],
    )
    move_cache()


image = (
    Image.from_registry("nvidia/cuda:12.1.0-base-ubuntu22.04", add_python="3.10")
    .pip_install(
        "vllm==0.2.5",
        "huggingface_hub==0.19.4",
        "hf-transfer==0.1.4",
        "torch==2.1.2",
    )
    # Use the barebones hf-transfer package for maximum download speeds. No progress bar, but expect 700MB/s.
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model_to_folder,
        secret=Secret.from_name("HF_TOKEN"),
        timeout=5000,
    )
)

stub = Stub("example-vllm-inference", image=image)


@stub.cls(gpu="A100", secret=Secret.from_name("HF_TOKEN"), timeout=5000)
class Model:
    def __enter__(self):
        from vllm import LLM

        self.llm = LLM(MODEL_DIR)
        self.template = """<s>[INST] <<SYS>>
{system}
<</SYS>>

{user} [/INST] """

    @method()
    def generate(self, df):
        from vllm import SamplingParams

        sampling_params = SamplingParams(
            temperature=0.75,
            top_p=1,
            max_tokens=800,
            presence_penalty=1.15,
        )
        prompts = df["scoring_template"]
        result = self.llm.generate(prompts, sampling_params)
        outputlist = [i.outputs[0].text for i in result]

        # for output in result:
            # num_tokens += len(output.outputs[0].token_ids)

        df.loc[:, "scoring_response"] = outputlist
        return df


@stub.local_entrypoint()
def main():
    model = Model()
    import pandas as pd

    filename = "dolly-15k-quality.csv"
    df = pd.read_csv(filename, dtype=str)
    df = model.generate.remote(df)
    df.to_csv(filename)
