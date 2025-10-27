import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ace_core.llm import llm
from langchain_core.messages import AIMessage


def test_llm_instance():
    assert llm is not None
    assert hasattr(llm, "invoke")

def test_llm_response():
    response = llm.invoke("Just say 'hello'.")
    assert isinstance(response, AIMessage)
    assert response.content.lower() == "hello"