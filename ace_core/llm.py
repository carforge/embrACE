from langchain_ollama import ChatOllama

llm = ChatOllama(
    base_url="http://192.168.200.160:11434",
    model="gpt-oss:20b"
)