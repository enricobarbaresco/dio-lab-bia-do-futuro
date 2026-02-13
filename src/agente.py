import requests
import json
from config import carregar_dados

def gerar_resposta_invest(pergunta_usuario):
    dados_contexto = carregar_dados()
    
    # Construção do Prompt (RAG)
    prompt_sistema = f"""
    Você é o FinAI, um assistente de investimentos altamente seguro e preciso.
    Dados atuais do cliente:
    - Saldo em conta: R$ {dados_contexto.get('saldo_total', 0)}
    - Perfil: {dados_contexto.get('perfil', {}).get('perfil', 'Não definido')}
    - Objetivo: {dados_contexto.get('perfil', {}).get('objetivo', 'Não definido')}
    
    Regra: Se o perfil for Conservador, nunca sugira Criptomoedas ou Ações voláteis.
    Responda sempre de forma curta e baseada nos dados fornecidos.
    """

    payload = {
        "model": "llama3",
        "prompt": f"{prompt_sistema}\nUsuário: {pergunta_usuario}\nAssistente:",
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        return response.json().get('response', "Erro ao processar resposta.")
    except Exception as e:
        return f"Erro de conexão com Ollama: {e}"
