from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import create_tool_calling_agent
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import MessagesPlaceholder

from ace_core.llm import llm
from ace_core.tools import tools
from ace_core.memory import InMemoryChatHistory

# Create the agent
agent_runnable: Runnable = create_tool_calling_agent(llm=llm, tools=tools)

# Create the executor with memory
chat_history = InMemoryChatHistory()

agent_executor = AgentExecutor(
    agent=agent_runnable,
    tools=tools,
    handle_parsing_errors=True,
)

# Optional: wrapper function to run agent with memory
def run_agent(user_input: str) -> str:
    chat_history.add_user_message(user_input)
    response = agent_executor.invoke({"input": user_input, "chat_history": chat_history.get_messages()})
    chat_history.add_ai_message(response["output"])
    return response["output"]