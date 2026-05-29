from langchain_core.tools import tool
from tools.tavily_search import search_web

@tool
def search_agent(query: str) -> list:
    """Search the web for the given query and return the result"""
    results = search_web(query)
    return results