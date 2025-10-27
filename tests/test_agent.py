import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_core.messages import AIMessage, HumanMessage

from ace_core.agent import run_agent

def test_run_agent_response():
    response = run_agent("My name is Yannic")
    assert isinstance(response, dict)
    assert len(response) > 0