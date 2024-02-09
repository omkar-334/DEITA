import os

from modal import Image, Secret, Stub, method

MODEL_DIR = "/model"
BASE_MODEL = "satpalsr/llama2-translation-filter-full"

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

stub = Stub("", image=image)

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
    def generate(self,prompts, actual_values):
        from vllm import SamplingParams

        sampling_params = SamplingParams(
            temperature=0.75,
            top_p=1,
            max_tokens=800,
            presence_penalty=1.15,
        )
        result = self.llm.generate(prompts, sampling_params)
        num_tokens = 0
        correct_predictions=0
        total_predictions=len(prompts)
        for output, check in zip(result,actual_values):
            # num_tokens += len(output.outputs[0].token_ids)
            # print(output.prompt, output.outputs[0].text, "\n\n", sep="")
            if check in output.outputs[0].text:
                correct_predictions+=1
        # print(f"Generated {num_tokens} tokens")
        print(f"Correct Predictions - {correct_predictions}")
        print(f"Total Predictions - {total_predictions}")
        print(f"Accuracy - {correct_predictions/total_predictions}")


@stub.local_entrypoint()
def main():
    from datasets import load_dataset
    v_dataset = load_dataset("satpalsr/chatml-translation-filter",split='validation')

    template = """<|im_start|>system
For a given question assess whether translating the potential answer to another language might yield an inaccurate response. Avoid translation in tasks related to coding problems, alliteration, idioms, paraphrasing text, word count, spelling correction, and other linguistic constructs or contextual nuances that may affect the accuracy of the answer. When translation is deemed unsuitable, output {\"translate\": False}. Otherwise, output {\"translate\": True}.<|im_end|>
<|im_start|>user
"""

    prompts=[template+i[1]['value']+"<|im_end|>\n<|im_start|>assistant\n" for i in v_dataset['conversations']]
    actual_values=[i[2]['value'] for i in v_dataset['conversations']]

    model = Model()
    model.generate.remote(prompts, actual_values)    model = Model()
    model.generate.remote(prompts, actual_values)