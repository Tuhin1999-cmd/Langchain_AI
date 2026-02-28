
import os
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from information import getinformation
from prompttemplate import system_prompt

# model switiching has been faster in groq, it is an interface
# can't use any own deployed model or own hardware model only can use models hosted in groq hardware 


class GroqExtended:

    @staticmethod
    def chat_ollama():
        
        #llm = ChatOllama(
        #     model="gemma3:270m",
        #     temperature=0
        # )

        llm = ChatGroq(
            model = 'llama-3.1-8b-instant',
            temperature = 0
        )

        return llm
    
    @staticmethod
    def chat_gemini():

        # llm = ChatGoogleGenerativeAI(
        #         model="gemini-3-flash-preview",
        #         google_api_key=os.environ.get("GOOGLE_API_KEY"),
        #     )

        llm = ChatGroq(
            model = 'openai/gpt-oss-120b',
        )

        return llm
    
    @staticmethod
    def invoke(llm, ):

        info = getinformation()

        summary_prompt_template = PromptTemplate(input_variables = [info] , template = system_prompt)
        
        chain = summary_prompt_template | llm | StrOutputParser()
    
        response = chain.invoke({
            "info" : info
        })

        return response
