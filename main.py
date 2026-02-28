import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from prompttemplate import system_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from information import getinformation
from prompttemplate import system_prompt

load_dotenv()

def main():
    
    info = getinformation()
    
    summary_prompt_template = PromptTemplate(input_variables = [info] , template = system_prompt)
    
    # llm = ChatGoogleGenerativeAI(
    #         model="gemini-3-flash-preview",
    #         google_api_key=os.environ.get("GOOGLE_API_KEY"),
    #     )

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0
    )
    
    chain = summary_prompt_template | llm | StrOutputParser()
    response = chain.invoke({
        "info" : info
    })
    
    print(response)

if __name__ == "__main__":
    main()
