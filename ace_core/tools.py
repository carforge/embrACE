from langchain.agents import Tool
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

search_tool = TavilySearchResults()

tools = [
    Tool.from_function(greet),
    search_tool
]