from datasets import load_dataset
import pandas as pd
# dataset = load_dataset("databricks/databricks-dolly-15k",split='train')

dataset = load_dataset("hkust-nlp/deita-6k-v0",split="train")
print(dataset)
df=pd.DataFrame(dataset)
print(df['conversations'][1])