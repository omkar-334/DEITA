import pandas as pd
from datasets import load_dataset

# dataset = load_dataset("databricks/databricks-dolly-15k",split='train')
# df=pd.DataFrame(dataset['instruction'],columns=["instruction"])

filename = "dolly-15k-quality.csv"
df = pd.read_csv(filename)

helpfulness_template = """I want you to act as a Response Rewriter.
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You Should enhance the quality of the response using the following method:
Please make the Response more helpful to the user.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#.
#Given Prompt#:
"""

relevance_template = """I want you to act as a Response Rewriter.
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You should enhance the quality of the response using the following method:
Please make the Response more relevant to #Given Prompt#.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#
#Given Prompt#:
"""

depth_template = """I want you to act as a Response Rewriter
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You Should enhance the quality of the response using the following method:
Please make the Response more in-depth.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#.
#Given Prompt#:
"""

creativity_template = """I want you to act as a Response Rewriter
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You Should enhance the quality of the response using the following method:
Please increase the creativity of the response.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#
#Given Prompt#:
"""

details_template = """I want you to act as a Response Rewriter
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You Should enhance the quality of the response using the following method:
Please increase the detail level of Response.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#.
#Given Prompt#:
"""

df["helpfulness_template"] = (
    helpfulness_template
    + df["instruction"]
    + "\n\n#Given Response#:"
    + df["response"]
    + "\n\n#Rewritten Response:"
)
df["helpfulness_response"] = ""

df["relevance_template"] = (
    relevance_template
    + df["instruction"]
    + "\n\n#Given Response#:"
    + df["response"]
    + "\n\n#Rewritten Response:"
)
df["relevance_response"] = ""

df["depth_template"] = (
    depth_template
    + df["instruction"]
    + "\n\n#Given Response#:"
    + df["response"]
    + "\n\n#Rewritten Response:"
)
df["depth_response"] = ""

df["creativity_template"] = (
    creativity_template
    + df["instruction"]
    + "\n\n#Given Response#:"
    + df["response"]
    + "\n\n#Rewritten Response:"
)
df["creativity_response"] = ""

df["details_template"] = (
    details_template
    + df["instruction"]
    + "\n\n#Given Response#:"
    + df["response"]
    + "\n\n#Rewritten Response:"
)
df["details_response"] = ""

df.to_csv(filename)
