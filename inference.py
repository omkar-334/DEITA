import os

import modal

MODEL_DIR = "/model"
MODEL_NAME = "meta-llama/Meta-Llama-3-8B"


# Tip: avoid using global variables in this function.
# Changes to code outside this function will not be detected, and the download step will not re-run.
def download_model_to_image(model_dir, model_name):
    from huggingface_hub import snapshot_download
    from transformers.utils import move_cache

    os.makedirs(model_dir, exist_ok=True)

    snapshot_download(
        model_name,
        local_dir=model_dir,
        ignore_patterns=["*.pt", "*.bin"],  # Using safetensors
        token=os.environ["HF_TOKEN"],
    )
    move_cache()


image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install("vllm==0.4.0.post1", "torch==2.1.2", "transformers==4.39.3", "ray==2.10.0", "hf-transfer==0.1.6", "huggingface_hub==0.22.2", "pandas")
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
    .run_function(
        download_model_to_image,
        timeout=5000,
        kwargs={"model_dir": MODEL_DIR, "model_name": MODEL_NAME},
        secrets=[modal.Secret.from_name("HF_TOKEN")],
    )
)

app = modal.App("llama3", image=image)


with image.imports():
    import pandas as pd
    import vllm

# Hint: try out an H100 if you've got a large model or big batches!
GPU_CONFIG = modal.gpu.H100(count=1)  # 40GB A100 by default


@app.cls(gpu=GPU_CONFIG, timeout=5000)
class Model:
    @modal.enter()
    def load_model(self):
        # Tip: models that are not fully implemented by Hugging Face may require `trust_remote_code=true`.
        self.llm = vllm.LLM(MODEL_DIR, tensor_parallel_size=GPU_CONFIG.count)

    @modal.method()
    def generate(self, df):
        sampling_params = vllm.SamplingParams(
            temperature=0.8,
            top_p=1,
            max_tokens=512,
            presence_penalty=1.15,
        )

        prompts = df["reasoning_instruction"]

        result = self.llm.generate(prompts, sampling_params)
        outputlist = [i.outputs[0].text for i in result]
        df.loc[:, "reasoning_response"] = outputlist

        return df


@app.local_entrypoint()
def main():
    model = Model()
    import pandas as pd

    filename = "quality.csv"
    df = pd.read_csv(filename, dtype=str)
    df = model.generate.remote(df)

    outname = "quality1.csv"
    df.to_csv(outname)
