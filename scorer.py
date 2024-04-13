csample="""Ranking the following questions according to the difficulty and complexity. Score 1-5.
You can give a score of 6 if the question is too complex for you to answer it. You should respond with the format:\\n [1] Score: 1\\n [2] Score: 2\\n
[1] <Instruction 1>
[2] <Instruction 2>
[3] <Instruction 3>
[4] <Instruction 4>
[5] <Instruction 5>"""

qsample = """Rank the following responses provided by different AI assistants to the user's question according to the quality of their response. Score each response from 1 to 5, with 6
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

cscore ="""Rank the following questions according to the difficulty and complexity. Score 1-5.
You can give a score of 6 if the question is too complex for you to answer it.
[1]: {}
[2]: {}
[3]: {}
[4]: {}
[5]: {}

Do not include any explanation or reasons in the scoring. Do not add any additional details. Strictly follow the scoring template given below. 
You should respond with the format:
[1] Score: _
[2] Score: _
[3] Score: _
[4] Score: _
[5] Score: _"""

qscore = """Rank the following responses provided by different AI assistants to the user's question
according to the quality of their response. Score each response from 1 to 5, with 6
reserved for responses that are already very well written and cannot be improved further.
Your evaluation should consider factors such as helpfulness, relevance, accuracy, depth,
creativity, and level of detail of the response.

#Question#:
{}

#Response List#:
[1]: {}
[2]: {}
[3]: {}
[4]: {}
[5]: {}
[6]: {}

Do not include any explanation or reasons in the scoring. Do not add any additional details. Strictly follow the scoring template given below. You should respond with the format: 
[1] Score: _
[2] Score: _
[3] Score: _
[4] Score: _
[5] Score: _
[6] Score: _"""

def complexity_scorer(instruction : str, responses : list[str]):
    out = cscore.format(instruction, *responses)
    # out = out.replace(r"].{0,3}\n","]",regex=True)
    # out = out.replace(r"#Given[\s\S]*?\[",'[',regex=True)
    return out

def quality_scorer(instruction : str, responses : list[str]):
    out = qscore.format(instruction, *responses)
    # out = out.replace(r"].{0,3}\n", "]", regex=True)
    return out
    