from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from ace_core.llm import llm
from ace_core.tools import tools
from ace_core.memory import InMemoryChatHistory

# Create the agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant."
)

# Create memory
chat_history = InMemoryChatHistory()

# Run the agent
def run_agent(user_input: str) -> str:
    chat_history.add_user_message(user_input)
    response = agent.invoke({
        "messages": chat_history.get_messages()
    })
    if isinstance(response["messages"][-1], AIMessage):
        chat_history.add_ai_message(response["messages"][-1].content)
    return response