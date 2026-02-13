import streamlit as st
from agente import gerar_resposta_invest

st.set_page_config(page_title="FinAI Invest", page_icon="💰")

st.title("💰 FinAI Invest - Seu Assistente Local")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Como posso ajudar seus investimentos hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        resposta = gerar_resposta_invest(prompt)
        st.markdown(resposta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
