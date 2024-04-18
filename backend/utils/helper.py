import json
import os
from typing import Any

import openai
from dotenv import load_dotenv
import logging

from langchain.chains import LLMChain, GraphCypherQAChain
from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph

from .customprompt import (
    PROJECT_UNDERSTANDING_PROMPT,
    PROMPT_PROJECT_EXPLANATION,
    PROMPT_FUNCTION_EXPLANATION_TECHNICAL,
    PROMPT_FUNCTION_EXPLANATION_FUNCTIONAL
)


class LLMHelper:
    def __init__(self,
                 llm_for_explanation: ChatOpenAI = None,
                 llm_for_project: ChatOpenAI = None,
                 llm_for_cypher: ChatOpenAI = None,
                 temperature: float = None,
                 max_tokens: int = None
                 ):

        load_dotenv()
        openai.api_type = "azure"
        openai.api_base = os.getenv('OPENAI_API_BASE')
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Azure OpenAI settings
        self.api_base = openai.api_base
        self.api_version = openai.api_version
        self.model: str = os.getenv('OPENAI_EMBEDDINGS_ENGINE_DOC', "text-embedding-ada-002")
        self.deployment_name: str = os.getenv("OPENAI_ENGINE", os.getenv("OPENAI_ENGINES", "gpt-4-32k"))
        self.temperature: float = float(os.getenv("OPENAI_TEMPERATURE", 0.7)) if temperature is None else temperature
        self.max_tokens: int = int(os.getenv("OPENAI_MAX_TOKENS", -1)) if max_tokens is None else max_tokens
        self.usernameNeo4j: str = os.getenv("LOGIN_NEO4J", "neo4j")
        self.passwordNeo4j: str = os.getenv("PASSWORD_NEO4J", "pleaseletmein")
        self.urlNeo4j: str = os.getenv("URL_NEO4J", "bolt://localhost:7687")

        # LLM initialization upon the needs
        self.llm_for_explanation: ChatOpenAI = ChatOpenAI(
            model_name=self.deployment_name,
            temperature=self.temperature,
            model_kwargs={
                "engine": self.deployment_name
            }
        ) if llm_for_explanation is None else llm_for_explanation

        self.llm_for_project: ChatOpenAI = ChatOpenAI(
            model_name=self.deployment_name,
            temperature=0.5,
            model_kwargs={
                "engine": self.deployment_name
            }
        ) if llm_for_project is None else llm_for_project

        self.llm_for_cypher: ChatOpenAI = ChatOpenAI(
            model_name=self.deployment_name,
            temperature=0,
            model_kwargs={
                "engine": self.deployment_name
            }
        ) if llm_for_cypher is None else llm_for_cypher

    def get_connection_neo4j(self):
        """
        Get connection for neo4j
        :return:
        :rtype: str
        """
        return Neo4jGraph(
            url=self.urlNeo4j, username=self.usernameNeo4j, password=self.passwordNeo4j
        )

    def explaining_project(self, input_code: list, explanation_difficulty: str) -> tuple[str, list[Any]]:
        """
        Neo4j graph approach to explain the project
        :param input_code: List of files
        :type input_code: list
        :param explanation_difficulty: Level of explanation
        :type explanation_difficulty: str
        :return: Return the explanation of the project
        :rtype: str
        """
        try:
            responses_tot = []
            node_list = []
            links_list = []
            branches_query = []
            responses_function_tot_functional = []
            responses_function_tot_technical = []

            graph = Neo4jGraph(
                url=self.urlNeo4j, username=self.usernameNeo4j, password=self.passwordNeo4j
            )

            json_template = """
            {
                {
                   "Type": "",
                   "Name": "",
                   "Dependency": [""],
                   "Objective_functional": "",
                   "Objective_technical": "",
                   "Branch_name": "",
                   "File_definition": ""
                }
            }
            """
            cpt = 0
            for code in input_code:
                cpt = cpt + 1

                result = LLMChain(
                    prompt=PROMPT_PROJECT_EXPLANATION,
                    llm=self.llm_for_project,
                    verbose=True
                ).run(
                    input_code=code,
                    json_template=json_template
                )
                try:
                    responses_tot.append(json.loads(result))
                except Exception:
                    pass

                result_function_functional = LLMChain(
                    prompt=PROMPT_FUNCTION_EXPLANATION_FUNCTIONAL,
                    llm=self.llm_for_project,
                    verbose=True
                ).run(
                    code=code,
                    explaination_difficulty=explanation_difficulty,
                    json_template="""{
                                    "general": {
                                       "file_name": "",
                                       "langage": "",
                                       "simple_explanation": ""
                                       },
                                    "explanation_text": "",
                                    "fonction_tab": [{
                                       "fonction_name": "",
                                       "description": "",
                                       "arguments": [{
                                          "arg_name": "",
                                          "arg_type": "",
                                          "arg_description": ""
                                       }],
                                       "dependance": []
                                     }]
                                    }"""
                )
                try:
                    responses_function_tot_functional.append(json.loads(result_function_functional))
                except:
                    pass

                # result_function_technical = LLMChain(
                #     prompt=PROMPT_FUNCTION_EXPLANATION_TECHNICAL,
                #     llm=self.llm_for_project,
                #     verbose=False
                # ).run(
                #     code=code,
                #     explaination_difficulty=explanation_difficulty,
                #     json_template="""{
                #                     "general": {
                #                        "file_name": "",
                #                        "langage": "",
                #                        "simple_explanation": ""
                #                        },
                #                     "explanation_text": "",
                #                     "fonction_tab": [{
                #                        "fonction_name": "",
                #                        "description": "",
                #                        "arguments": [{
                #                           "arg_name": "",
                #                           "arg_type": "",
                #                           "arg_description": ""
                #                        }],
                #                        "dependance": []
                #                      }]
                #                     }"""
                # )
                # responses_function_tot_technical.append(json.loads(result_function_technical))

            complete_list = [element for sub_list in responses_tot for element in sub_list]

            for element in complete_list:
                dependencies = []
                for dependency in element["Dependency"]:
                    if "." in dependency:
                        dependencies.append(dependency.split(".")[1])

                if dependencies:
                    element["Dependency"] = dependencies

                node_list.append(
                    '(' + element["Name"] +
                    ':' + element["Type"] +
                    ' {name:"' + element["Name"] +
                    '", objective_technical:"' + element["Objective_technical"] +
                    '", objective_functional:"' + element["Objective_functional"] +
                    '", file_name:"' + element["File_definition"] +
                    '"})')

            for elements in node_list:
                cypher_query_nodes = "CREATE " + elements
                graph.query(cypher_query_nodes)

            for branches, nodes in zip(complete_list, node_list):
                for dependencies in branches["Dependency"]:
                    dependencies_dict = {
                        "dependency_function": dependencies,
                        "query_from": nodes,
                        "type_relation": branches["Branch_name"],
                        "depended_function": branches["Name"]
                    }

                    links_list.append(dependencies_dict)

            for links_creation in links_list:
                for elements in node_list:
                    if links_creation["dependency_function"] in elements:
                        query_branches = 'MATCH ' \
                                         + links_creation["query_from"] \
                                         + ', ' \
                                         + elements \
                                         + ' CREATE (' \
                                         + links_creation["depended_function"] \
                                         + ')-[:' \
                                         + links_creation["type_relation"] \
                                         + ']->' \
                                         + '(' + links_creation["dependency_function"] + ')'
                        branches_query.append(query_branches)

            for branch_setting in list(set(branches_query)):
                graph.query(branch_setting)

            graph.refresh_schema()

            graph.query(
                "MATCH (n) WHERE NOT "
                "(n.name IS NOT NULL AND "
                "n.objective_technical IS NOT NULL AND "
                "n.objective_functional IS NOT NULL AND "
                "n.file_name IS NOT NULL) "
                "DETACH DELETE n"
            )

            graph.query(
                "MATCH (n:FUNCTION) "
                "WITH n.name AS name, collect(n) AS nodelist, count(*) AS count "
                "WHERE count > 1 "
                "UNWIND tail(nodelist) AS nodeToDelete "
                "DETACH "
                "DELETE nodeToDelete"
            )

            graph.query(
                "MATCH (n:CLASS) "
                "WITH n.name AS name, collect(n) AS nodelist, count(*) AS count "
                "WHERE count > 1 "
                "UNWIND tail(nodelist) AS nodeToDelete "
                "DETACH "
                "DELETE nodeToDelete"
            )

            graph.query(
                "MATCH (n:INTERFACE) "
                "WITH n.name AS name, collect(n) AS nodelist, count(*) AS count "
                "WHERE count > 1 "
                "UNWIND tail(nodelist) AS nodeToDelete "
                "DETACH "
                "DELETE nodeToDelete"
            )

            graph.query(
                "MATCH (n:FILE) "
                "WITH n.name AS name, collect(n) AS nodelist, count(*) AS count "
                "WHERE count > 1 "
                "UNWIND tail(nodelist) AS nodeToDelete "
                "DETACH "
                "DELETE nodeToDelete"
            )

            graph.query(
                "MATCH (n)-[r:HAS]-(n) "
                "DELETE r"
            )

            graph.query(
                "MATCH (n)-[r:DEFINED]-(n) "
                "DELETE r"
            )

            graph.query(
                "MATCH (n)-[r:DEPENDS_ON]-(n) "
                "DELETE r"
            )

            graph.refresh_schema()

            response = GraphCypherQAChain.from_llm(
                cypher_llm=self.llm_for_cypher,
                qa_llm=self.llm_for_explanation,
                llm=self.llm_for_explanation,
                qa_prompt=PROJECT_UNDERSTANDING_PROMPT,
                graph=graph,
                verbose=True,
                top_k=-1,
                return_intermediate_steps=True,
            ).run(
                "You are a business analyst, summarize all the objective_functional mostly on the nodes FILE present"
                "as if it was to write the introduction"
                "of a functional user guide. Do not get too technical, express the overall objective of "
                "this application described by these objectives. "
                "Also see the nodes and branches and try to give me a good explanation"
                "The application has been convert it into graph so I want the information on my application"
                "The property existence syntax `... exists(variable.property)` is no longer supported. "
                "Please use `variable.property IS NOT NULL` instead."
                f"And can you give me the purpose of the application "
                f"base on the different objective for a {explanation_difficulty} public"
                "In the summary, don't explain me technically but more functionally as this text will be read by final "
                "users who are not IT people"
                "Note: Give me only the summary nothing else"
            )

            return response, responses_function_tot_functional
        except Exception as e:
            logging.error(f"Error generating code: {e}")

    def get_function_details(self, question: str, chat_history: str):
        try:
            graph = Neo4jGraph(
                url=self.urlNeo4j, username=self.usernameNeo4j, password=self.passwordNeo4j
            )

            response = GraphCypherQAChain.from_llm(
                cypher_llm=self.llm_for_cypher,
                qa_llm=self.llm_for_explanation,
                llm=self.llm_for_explanation,
                qa_prompt=PROJECT_UNDERSTANDING_PROMPT,
                graph=graph,
                verbose=True,
                top_k=-1,
                return_intermediate_steps=True,
            ).run(
                "The property existence syntax `... exists(variable.property)` is no longer supported. "
                "Please use `variable.property IS NOT NULL` instead."
                f"This is what the user asked for before {chat_history}"
                f"And they what this {question}"
            )

            return response
        except Exception as e:
            logging.error(f"Error generating code: {e}")
