from langchain_community.llms import Ollama

llm = Ollama(
    base_url="http://192.168.200.160",
    model="gemma:27b"
)
