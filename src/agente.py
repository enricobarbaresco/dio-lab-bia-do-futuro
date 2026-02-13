import requests
from config import carregar_contexto

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"

SYSTEM_PROMPT = """Você é o FinAI Invest, um Agente Financeiro Inteligente especializado em RAG. 
Sua missão é ajudar o usuário com base estrita nos dados fornecidos."""

def perguntar(msg):
    contexto = carregar_contexto()
    prompt_completo = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"
    
    payload = {
        "model": MODELO, 
        "prompt": prompt_completo, 
        "stream": False
    }
    
    try:
        r = requests.post(OLLAMA_URL, json=payload)
        return r.json()['response']
    except Exception as e:
        return f"Erro ao conectar com Ollama: {e}"
