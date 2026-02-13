import json
import pandas as pd
import requests
import streamlit as st
import os

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3"  # <--- Verifique se é este o nome no seu Ollama
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

# ============ CARREGAR DADOS ============
perfil = json.load(open(os.path.join(DATA_DIR, 'perfil_investidor.json'), encoding='utf-8'))
transacoes = pd.read_csv(os.path.join(DATA_DIR, 'transacoes.csv'))
historico = pd.read_csv(os.path.join(DATA_DIR, 'historico_atendimento.csv'))
produtos = json.load(open(os.path.join(DATA_DIR, 'produtos_financeiros.json'), encoding='utf-8'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o FinAI Invest, um Agente Financeiro Inteligente...""" # (Mantenha seu texto aqui)

# ============ FUNÇÃO DE PERGUNTA ============
def perguntar(msg):
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO DO CLIENTE:\n{contexto}\n\nPergunta: {msg}"
    
    try:
        r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
        return r.json()['response']
    except Exception as e:
        return f"Erro ao conectar com Ollama: {e}"

# ============ INTERFACE STREAMLIT ============
st.title("FinAI Invest, Seu Educador Financeiro!")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Consultando dados..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
