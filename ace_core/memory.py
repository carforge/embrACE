from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage

class InMemoryChatHistory(BaseChatMessageHistory):
    def __init__(self):
        self.messages = []

    def add_user_message(self, message: str) -> None:
        self.messages.append(HumanMessage(content=message))

    def add_ai_message(self, message: str) -> None:
        self.messages.append(AIMessage(content=message))

    def get_messages(self):
        return self.messages

    def clear(self):
        self.messages = []