import os

from dotenv import load_dotenv
from GroqExtended import GroqExtended
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from information import getinformation
from prompttemplate import system_prompt
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from search import search
from langchain_tavily import TavilySearch

load_dotenv()

def main():
    
    llm = GroqExtended.chat_ollama()

    tools = [search.search_data] # this is custom logic

    # tools = [TavilySearch()] this is more accurate as the tavily library has better tools

    agent = create_agent(tools=tools, model=llm)

    result = agent.invoke({
        "messages": HumanMessage(content="find me 3 relevant jobs as my skill is asp.net in india")
    })

    print(result)



if __name__ == "__main__":
    main()
