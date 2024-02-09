import re

import numpy as np
import pandas as pd
import pandas as pd

filename = "dolly-15k-complexity.csv"
df = pd.read_csv(filename, dtype=str)

pattern = r'\[[1]\]\s*Score:\s*[0-9]\s*\[[2]\]\s*Score:\s*[0-9]\s*\[[3]\]\s*Score:\s*[0-9]\s*\[[4]\]\s*Score:\s*[0-9]\s*\[[5]\]\s*Score:\s*[0-9]'
pattern1 = r'\[[0-9]\]\s*Score:\s*[0-9]'
pattern2 = r'\[[0-9]\]\s*[0-9]'


def cleaner(text):
    temp=re.findall(pattern1, text)
    if not temp:
        temp=re.findall(pattern2, text)

    out = [i[-1] for i in temp]
    if len(out) == 10:
        if out[:5] == out[5:]:
            out=out[:5]
    if len(out) != 5:
        return None
    return out
cleanerx=np.vectorize(cleaner)

df['finalscores']=df['scoring_response'].map(cleanerx)

# df[df['finalscores'].str.len()!=5].to_csv("newnull.csv")
# df[df.isna().any(axis=1)].info()
# df[df['finalscores'].str.len()!=5]['finalscores'].head(20)
# df['finalscores'].head()

tempdf = df[df['finalscores'].notnull()][['instruction','reasoning_response','constraints_response', 'deepening_response', 'concretizing_response', 'finalscores']]
scores1=tempdf['finalscores'].map(lambda x:x[0])
scores2=tempdf['finalscores'].map(lambda x:x[1])
scores3=tempdf['finalscores'].map(lambda x:x[2])
scores4=tempdf['finalscores'].map(lambda x:x[3])
scores5=tempdf['finalscores'].map(lambda x:x[4])
tempdf.reset_index(inplace=True,drop=True)

prompts = tempdf['instruction'].tolist() + tempdf['reasoning_response'].tolist() + tempdf['constraints_response'].tolist() + tempdf['deepening_response'].tolist() + tempdf['concretizing_response'].tolist()
scores = scores1.tolist() + scores2.tolist() + scores3.tolist() + scores4.tolist() + scores5.tolist()

outdf=pd.DataFrame({'prompt':prompts,"score":scores})
outdf.to_csv('complexity.csv')