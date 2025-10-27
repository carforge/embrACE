from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    base_url="http://192.168.200.160:11434",
    model="gemma2:27b"
)