import pandas as pd
filename="dolly-15k-complexity.csv"
df=pd.read_csv(filename,dtype=str)

sample="""Ranking the following questions according to the difficulty and complexity. Score 1-5.
You can give a score of 6 if the question is too complex for you to answer it. You should
respond with the format:\\n [1] Score: 1\\n [2] Score: 2\\n
[1] <Instruction 1>
[2] <Instruction 2>
[3] <Instruction 3>
[4] <Instruction 4>
[5] <Instruction 5>"""


scoring_template="""Rank the following questions according to the difficulty and complexity. Score 1-5.
You can give a score of 6 if the question is too complex for you to answer it. \n"""

end_template = """\n\n Do not include any explanation or reasons in the scoring. Do not add any additional details. Strictly follow the scoring template given below. You should respond with the format:\n [1] Score: _\n [2] Score: _\n [3] Score: _\n [4] Score: _\n [5] Score: _\n"""

df['scoring_template']=scoring_template +"\n[1]\n" + df['instruction'] + "\n[2]" + df['reasoning_response'] + "\n[3] " + df['constraints_response'] + "\n[4] " + df['deepening_response'] + "\n[5] " + df['concretizing_response'] + end_template

df.scoring_template = df.scoring_template.str.replace(r"].{0,3}\n","]",regex=True)

df.scoring_template = df.scoring_template.str.replace(r"#Given[\s\S]*?\[",'[',regex=True)
df['scoring_response']=''

df.to_csv(filename)
