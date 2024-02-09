import pandas as pd

filename = "dolly-15k-quality.csv"
df = pd.read_csv(filename, dtype=str)

sample = """Rank the following responses provided by different AI assistants to the user's question according to the quality of their response. Score each response from 1 to 5, with 6
reserved for responses that are already very well written and cannot be improved further.
Your evaluation should consider factors such as helpfulness, relevance, accuracy, depth, creativity, and level of detail of the response.

#Question#: <Instruction>
#Response List#:
[1] <Response 1>
[2] <Response 2>
[3] <Response 3>
[4] <Response 4>
[5] <Response 5>
[6] <Response 6>"""

scoring_template = """Rank the following responses provided by different AI assistants to the user's question
according to the quality of their response. Score each response from 1 to 5, with 6
reserved for responses that are already very well written and cannot be improved further.
Your evaluation should consider factors such as helpfulness, relevance, accuracy, depth,
creativity, and level of detail of the response.

#Question#: """

end_template = """\n\n Do not include any explanation or reasons in the scoring. Do not add any additional details. Strictly follow the scoring template given below. You should respond with the format:\n [1] Score: _\n [2] Score: _\n [3] Score: _\n [4] Score: _\n [5] Score: _\n [6] Score: _\n"""

df["scoring_template"] = (
    scoring_template
    + df["instruction"]
    + "\n#Response List#:"
    + "\n\n[1]"
    + df["response"]
    + "\n\n[2] "
    + df["helpfulness_response"]
    + "\n\n[3] "
    + df["relevance_response"]
    + "\n\n[4] "
    + df["depth_response"]
    + "\n\n[5] "
    + df["creativity_response"]
    + "\n\n[6] "
    + df["details_response"]
    + end_template
)

df.scoring_template = df.scoring_template.str.replace(r"].{0,3}\n", "]", regex=True)

# df.scoring_template = df.scoring_template.str.replace(r"#Given[\s\S]*?\[",'[',regex=True)
df["scoring_response"] = ""
df.to_csv(filename)
