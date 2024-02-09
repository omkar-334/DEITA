from datasets import load_dataset
import pandas as pd

dataset = load_dataset("databricks/databricks-dolly-15k",split='train')
df=pd.DataFrame(dataset['instruction'],columns=["instruction"])

reasoning_template ="""I want you act as a Prompt Rewriter.
Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
If #Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.

#Given Prompt#:
"""
constraints_template="""I want you act as a Prompt Rewriter.
Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
Please add one more constraints/requirements into #Given Prompt#.`
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.

#Given Prompt#:
"""
deepening_template="""I want you act as a Prompt Rewriter.
Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
If #Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.

#Given Prompt#:
"""
concretizing_template="""I want you act as a Prompt Rewriter.
Your objective is to rewrite a given prompt into a more complex version to make those famous AI systems (e.g., ChatGPT and GPT4) a bit harder to handle.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following methods:
Please replace general concepts with more specific concepts.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.

#Given Prompt#:
"""

df['reasoning_template']=reasoning_template+df['instruction']+"\n\n#Rewritten Prompt#:"
df['reasoning_response']=''
df['constraints_template']=constraints_template+df['instruction']+"\n\n#Rewritten Prompt#:"
df['constraints_response']=''
df['deepening_template']=deepening_template+df['instruction']+"\n\n#Rewritten Prompt#:"
df['deepening_response']=''
df['concretizing_template']=concretizing_template+df['instruction']+"\n\n#Rewritten Prompt#:"
df['concretizing_response']=''

df=df[['instruction','reasoning_template','reasoning_response','constraints_template','constraints_response','deepening_template','deepening_response','concretizing_template','concretizing_response']]
df.to_csv("dolly-15k.csv")
