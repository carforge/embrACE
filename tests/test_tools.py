import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ace_core.tools import tools


def test_tools_is_list():
    """Check that tools is a list and not empty."""
    assert isinstance(tools, list), "tools should be a list"
    assert len(tools) > 0, "tools list should not be empty"

def test_greet_tool_exists():
    """Check that the greet tool is registered."""
    greet_tool = next((t for t in tools if t.name == "greet"), None)
    assert greet_tool is not None, "greet tool should be in the tools list"

def test_greet_tool_output():
    """Check that the greet tool returns the correct greeting."""
    greet_tool = next((t for t in tools if t.name == "greet"), None)
    result = greet_tool.run("Yannic")
    assert result == "Hello, Yannic!", f"Expected 'Hello, Yannic!', got '{result}'"

def test_tavily_tool():
    tavily_tool = next((t for t in tools if "search" in t.name.lower()), None)
    assert tavily_tool is not None
    result = tavily_tool.run("What is LangChain?")
    assert isinstance(result, dict)
    assert "answer" in result
    assert isinstance(result["answer"], str) or result["answer"] is None
