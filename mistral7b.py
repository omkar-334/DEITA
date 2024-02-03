import os
from modal import Image, Secret, Stub, method
import time
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
    Image.from_registry(
        "nvidia/cuda:12.1.0-base-ubuntu22.04", add_python="3.10"
    )
    .pip_install("vllm==0.2.5", "huggingface_hub==0.19.4", "hf-transfer==0.1.4")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model_to_folder,
        secret=Secret.from_name("HF_TOKEN"),
        timeout=60 * 20,
    )
)

stub = Stub("example-vllm-inference", image=image)

@stub.cls(gpu="A100", secret=Secret.from_name("HF_TOKEN"))
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
        result = self.llm.generate(df['reasoning_template'], sampling_params)
        num_tokens = 0
        outputlist=[]
        for output in result:
            num_tokens += len(output.outputs[0].token_ids)
            print(output.prompt, output.outputs[0].text, "\n\n", sep="")
            outputlist+=output.outputs[0].text
        print(f"Generated {num_tokens} tokens")
        df['reasoning_response'][:10]=outputlist
        print(df.head(10))


@stub.local_entrypoint()
def main():
    global df
    model = Model()
    import pandas as pd
    df=pd.read_csv("dolly-15k-complexity.csv")
    model.generate.remote(df)