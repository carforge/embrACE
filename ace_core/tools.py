from langchain.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()


@tool
def greet(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"


# Tavily search tool
tavily_api_key = os.getenv("TAVILY_API_KEY")
search_tool = TavilySearch(tavily_api_key=tavily_api_key)


tools = [greet, search_tool]