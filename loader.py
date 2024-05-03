import pandas as pd
from datasets import load_dataset

from prompts import createComplexityPrompts, createQualityPrompts

dataset = load_dataset("databricks/databricks-dolly-15k", split="train")

qdf = pd.DataFrame(dataset)[["instruction", "context", "response"]]


def add_context(x):
    if x:
        return "Pay attention to the provided context in the prompt and answer accordingly. \n#Context:\n" + x
    return ""


# Assuming 'column' is the name of your column consisting of strings
qdf["context"] = qdf["context"].apply(add_context)

(qdf["reasoning_instruction"], qdf["constraints_instruction"], qdf["deepening_instruction"], qdf["concretizing_instruction"]) = zip(*qdf.apply(lambda x: createComplexityPrompts("", x["instruction"]), axis=1))

qdf["reasoning_response"] = ""
qdf["constraints_response"] = ""
qdf["deepening_response"] = ""
qdf["concretizing_response"] = ""

qdf.to_csv("quality.csv")
