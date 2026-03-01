
from langchain.tools import tool
from tavily import TavilyClient

class search:

    

    @staticmethod
    @tool
    def search_data(query: str) -> str:
        """
        Tool that search over internet 
        Args :
            query : The query to search for text
        returns:
            The result return
        """
        
        print(f"searching on the web for : {query}")

        tavily = TavilyClient()
        
        response = tavily.search(query=query)

        return response