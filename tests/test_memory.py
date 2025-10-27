import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_core.messages import HumanMessage, AIMessage
from ace_core.memory import InMemoryChatHistory


def test_initial_state():
    """Ensure chat history starts empty."""
    history = InMemoryChatHistory()
    assert history.get_messages() == []

def test_add_user_message():
    """Test adding a user message."""
    history = InMemoryChatHistory()
    history.add_user_message("Hello!")
    messages = history.get_messages()
    assert isinstance(messages[0], HumanMessage)
    assert messages[0].content == "Hello!"

def test_add_ai_message():
    """Test adding an AI message."""
    history = InMemoryChatHistory()
    history.add_ai_message("Hi there!")
    messages = history.get_messages()
    assert isinstance(messages[0], AIMessage)
    assert messages[0].content == "Hi there!"

def test_message_order():
    """Ensure messages are stored in correct order."""
    history = InMemoryChatHistory()
    history.add_user_message("Hello!")
    history.add_ai_message("Hi!")
    messages = history.get_messages()
    assert isinstance(messages[0], HumanMessage)
    assert isinstance(messages[1], AIMessage)

def test_clear_history():
    """Test clearing the chat history."""
    history = InMemoryChatHistory()
    history.add_user_message("Hello!")
    history.clear()
    assert history.get_messages() == []