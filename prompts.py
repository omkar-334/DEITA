helpfulness = """I want you to act as a Response Rewriter.
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You Should enhance the quality of the response using the following method:
Please make the Response more helpful to the user.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
Do not include any instructions or explanations.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#.

#Given Prompt#:
{}


#Given Response#:
{}

#Rewritten Response:
"""

relevance = """I want you to act as a Response Rewriter.
Your goal is to enhance the quality of the response given by an AI assistant to the #Given Prompt# through rewriting.
But the rewritten response must be reasonable and must be understood by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt# and #Given Response#.
Also, please do not omit the input in #Given Prompt#.
You should enhance the quality of the response using the following method:
Please make the Response more relevant to #Given Prompt#.
You should try your best not to make the #Rewritten Response# become verbose,
#Rewritten Response# can only add 10 to 20 words into #Given Response#.
Do not include any instructions or explanations.
'#Given Response#', '#Rewritten Response#', 'given response' and 'rewritten response' are not allowed to appear in #Rewritten Response#

#Given Prompt#:
{}


#Given Response#:
{}

#Rewritten Response:
"""

depth = """I want you to act as a Response Rewriter
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
{}


#Given Response#:
{}

#Rewritten Response:
"""

creativity = """I want you to act as a Response Rewriter
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
{}


#Given Response#:
{}

#Rewritten Response:
"""

details = """I want you to act as a Response Rewriter
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
{}


#Given Response#:
{}

#Rewritten Response:
"""


reasoning = """I want you to act as a Prompt Rewriter.
Your task is to enhance a provided prompt by introducing additional layers of complexity, aiming to challenge advanced AI systems such as ChatGPT,  GPT4 and Llama-3.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
If #Given Prompt# can be solved with just a few simple thinking processes, you can rewrite it to explicitly request multiple-step reasoning.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.
Do not include any instructions or explanations.
{}
#Given Prompt#:
{}

#Rewritten Prompt#:

"""
constraints = """I want you to act as a Prompt Rewriter.
Your task is to enhance a provided prompt by introducing additional layers of complexity, aiming to challenge advanced AI systems such as ChatGPT,  GPT4 and Llama-3.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
Please add one more constraints/requirements into #Given Prompt#.`
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.
Do not include any instructions or explanations.
{}
#Given Prompt#:
{}

#Rewritten Prompt#:
"""
deepening = """I want you to act as a Prompt Rewriter.
Your task is to enhance a provided prompt by introducing additional layers of complexity, aiming to challenge advanced AI systems such as ChatGPT,  GPT4 and Llama-3.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following method:
If #Given Prompt# contains inquiries about certain issues, the depth and breadth of the inquiry can be increased.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.
Do not include any instructions or explanations.
{}
#Given Prompt#:
{}

#Rewritten Prompt#:
"""
concretizing = """I want you to act as a Prompt Rewriter.
Your task is to enhance a provided prompt by introducing additional layers of complexity, aiming to challenge advanced AI systems such as ChatGPT,  GPT4 and Llama-3.
But the rewritten prompt must be reasonable and must be understood and responded by humans.
Your rewriting cannot omit the non-text parts such as the table and code in #Given Prompt#.
Also, please do not omit the input in #Given Prompt#.
You SHOULD complicate the given prompt using the following methods:
Please replace general concepts with more specific concepts.
You should try your best not to make the #Rewritten Prompt# become verbose, #Rewritten Prompt# can only add 10 to 20 words into #Given Prompt#.
'#Given Prompt#', '#Rewritten Prompt#', 'given prompt' and 'rewritten prompt' are not allowed to appear in #Rewritten Prompt#.
Do not include any instructions or explanations.
{}
#Given Prompt#:
{}

#Rewritten Prompt#:
"""

complexity_templates = [reasoning, constraints, deepening, concretizing]


def createComplexityPrompts(context, prompt):
    return (reasoning.format(context, prompt), constraints.format(context, prompt), deepening.format(context, prompt), concretizing.format(context, prompt))


quality_templates = [helpfulness, relevance, depth, creativity, details]


def createQualityPrompts(instruction, response):
    return (helpfulness.format(instruction, response), relevance.format(instruction, response), depth.format(instruction, response), creativity.format(instruction, response), details.format(instruction, response))
