import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ace_core.llm import llm


def test_llm_instance():
    assert llm is not None
    assert hasattr(llm, "invoke")

def test_llm_response():
    response = llm.invoke("Say hello in one sentence.")
    assert isinstance(response, str)
    assert len(response.strip()) > 0
