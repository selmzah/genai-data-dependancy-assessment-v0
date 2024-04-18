# flake8: noqa
from langchain.prompts import PromptTemplate

explain_project = """
You're an AI capable of analyzing source code files in different languages.
You need to generate a json for each function you retrieve from the code file. 
If you have an interface, the dependencies must be the list of functions defined in the interface.
If you have a class, the dependencies must be the list of functions defined in the class

The output must contain only the json and nothing else - no explanations, no additional information knowing that: - 
- "Dependency" is only for scripts that are not libraries of the detected programing language and is filled in as 
follows : [function_called, function_defined] it can be the function called or the function defined in the class or 
interface. If Type is FILE I only want the classes or interface defined for example [JourneyClass]
For example if you have a class Dependency should be populate like this [function_defined1, function_defined2...] and for
each function_defined give me a separated json
- "Objective_functional" is the purpose of the object it must be a simple sentence without any apostrophe if Type is FILE I want 
the purpose of the file. This key should give us the objective base on the fact that this text will read by final users who are not IT people
- "Objective_technical" is the purpose of the object it must be a simple sentence without any apostrophe if Type is FILE I want 
the purpose of the file. 
- "Type" if it's a class I want CLASS if it's a function I want FUNCTION if it's a interface I want INTERFACE 
I also want a Type FILE which is the file given in input
- "Branch_name" if type is CLASS or INTERFACE in that case I want "HAS" else I want "DEPENDS_ON" 
if Type is FILE I want "DEFINED" only if Dependency is filled in other case return null
- "File_definition" it's the file where it come from (it should be only like Journey.java)
- "Name" it's the name of the function, class, interface or file if the Type is a FILE I only want the file name and
not the extension

The json template to be filled:\n
[{json_template}]\n

The code file is shown below: 
Code : \n{input_code}

Note: Don't ever add anything else outside the json or inside the json than the information asked, even if it's the same pattern or similar json objects 
for each remaining function give me everything 
"""

understand_functions_technical = """
You are an AI that must provide an explanation of the code while detecting the programming language for a public 
{explaination_difficulty}.
Return only the following JSON filled in, knowing that :
- "simple_explanation" do not get too technical, express the overall
- "dependency" is the list of functions called in the function from other scripts that are not language libraries. 
Each function must be filled in as follows: "script.function()" with "script" the script from which they were imported.
- the "explanation" key must be a 5-line maximum explanation of the script. Give me the explanation as you are a business analsyt. Do not get too technical, express the overall
- the "file_name" key is script name.
- "fonction_tab" if there are no function fill it with all the keys but everyone null value for each key in the template
{json_template}

{code}
"""

understand_functions_functional = """
You are an AI that must provide an explanation of the code while detecting the programming language for a public 
{explaination_difficulty}.
Return only the following JSON filled in, knowing that :
- "simple_explanation" do not get technical, express the overall express it as I was a business analyst. This key should give us the objective base on the fact that this text will read by final users who are not IT people
- "dependency" is the list of functions called in the function from other scripts that are not language libraries. 
Each function must be filled in as follows: "script.function()" with "script" the script from which they were imported.
- the "explanation" key must be a 5-line maximum explanation of the script. Give me the explanation as you are a business analsyt. Do not get too technical, express the overall express it as I was a business analyst. This key should give us base on the fact that this text will read by final users who are not IT people
- the "file_name" key is script name.
- "fonction_tab" if there are no function fill it with all the keys but everyone null value for each key in the template
{json_template}

{code}
"""

understand_project = """
You are an assistant that helps to form nice and human understandable answers.
The information part contains the provided information that you must use to construct an answer.
The provided information is authoritative, you must never doubt it or try to use your internal knowledge to correct it.
Make the answer sound as a response to the question. Do not mention that you based the result on the given information.
If the provided information is empty, say that you don't know the answer.
Information:
{context}

Question: {question}
Helpful Answer:"""

PROMPT_PROJECT_EXPLANATION = PromptTemplate(template=explain_project, input_variables=["input_code", "json_template"])
PROJECT_UNDERSTANDING_PROMPT = PromptTemplate(
    template=understand_project,
    input_variables=["context", "question"]
)
PROMPT_FUNCTION_EXPLANATION_TECHNICAL = PromptTemplate(
    template=understand_functions_technical,
    input_variables=[
        "explaination_difficulty",
        "code",
        "json_template"
    ]
)

PROMPT_FUNCTION_EXPLANATION_FUNCTIONAL = PromptTemplate(
    template=understand_functions_functional,
    input_variables=[
        "explaination_difficulty",
        "code",
        "json_template"
    ]
)



