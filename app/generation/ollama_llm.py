from langchain_ollama import OllamaLLM

def load_llm():
    return OllamaLLM(
        model="phi3:mini",
        base_url="http://127.0.0.1:11434",
        temperature=0.1
    )