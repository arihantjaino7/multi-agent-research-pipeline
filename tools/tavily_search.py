from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key = os.getenv("TAVILY_API_KEY"))

def search_web(query: str) -> list:
    result = client.search(
        query = query,
        max_results = 5,
        search_depth ="advanced"
    )
    return result["results"]