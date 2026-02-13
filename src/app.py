import streamlit as st
from agente import perguntar

st.set_page_config(page_title="FinAI Invest", page_icon="📈")

st.title("📈 FinAI Invest")
st.subheader("Seu Educador Financeiro Inteligente")

# Inicializa o histórico se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Entrada do usuário
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    # Adiciona e mostra pergunta do usuário
    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)
    
    # Gera e mostra resposta da IA
    with st.spinner("Consultando dados e gerando recomendação..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
