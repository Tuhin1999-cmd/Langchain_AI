import os

from dotenv import load_dotenv
from GroqExtended import GroqExtended
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from information import getinformation
from prompttemplate import system_prompt

load_dotenv()

def main():
    
    llm = GroqExtended.chat_ollama()
    
    print(GroqExtended.invoke(llm))

    print(GroqExtended.invoke(llm))

if __name__ == "__main__":
    main()
