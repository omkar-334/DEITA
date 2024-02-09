import re

import numpy as np
import pandas as pd


filename = "dolly-15k-quality.csv"
df = pd.read_csv(filename, dtype=str)

# pattern1 = r'\[[1]\]\s*Score:\s*[0-9]'
pattern = r'\[[1]\]\s*Score:\s*[0-9]\s*\[[2]\]\s*Score:\s*[0-9]\s*\[[3]\]\s*Score:\s*[0-9]\s*\[[4]\]\s*Score:\s*[0-9]\s*\[[5]\]\s*Score:\s*[0-9]'
pattern1 = r'\[[0-9]\]\s*Score:\s*[0-9]'
pattern2 = r'\[[0-9]\]\s*[0-9]'


def cleaner(text):
    temp=re.findall(pattern1, text)
    if not temp:
        temp=re.findall(pattern2, text)

    out = [i[-1] for i in temp]
    if len(out) == 12:
        if out[:6] == out[6:]:
            out=out[:6]
    if len(out) != 6:
        return None
    return out

cleanerx=np.vectorize(cleaner)

df['finalscores']=df['scoring_response'].map(cleanerx)

tempdf = df[df['finalscores'].notnull()][['instruction', 'response','helpfulness_response','relevance_response','depth_response','creativity_response', 'details_response','finalscores']]

tempdf['response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['response']
tempdf['helpfulness_response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['helpfulness_response']
tempdf['relevance_response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['relevance_response']
tempdf['depth_response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['depth_response']
tempdf['creativity_response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['creativity_response']
tempdf['details_response'] = "#Question: \n" + tempdf['instruction'] + "\n\nResponse:" + tempdf['details_response']

scores1=tempdf['finalscores'].map(lambda x:x[0])
scores2=tempdf['finalscores'].map(lambda x:x[1])
scores3=tempdf['finalscores'].map(lambda x:x[2])
scores4=tempdf['finalscores'].map(lambda x:x[3])
scores5=tempdf['finalscores'].map(lambda x:x[4])
scores6=tempdf['finalscores'].map(lambda x:x[5])
tempdf.reset_index(inplace=True,drop=True)

prompts=tempdf['instruction'].tolist() + tempdf['helpfulness_response'].tolist() + tempdf['relevance_response'].tolist() + tempdf['depth_response'].tolist() + tempdf['creativity_response'].tolist() + tempdf['details_response'].tolist()
scores=scores1.tolist() + scores2.tolist() + scores3.tolist() + scores4.tolist() + scores5.tolist() + scores6.tolist()

outdf=pd.DataFrame({'prompt':prompts,"score":scores})
outdf.to_csv('quality.csv')