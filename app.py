import streamlit as st
from load_csv import load_data
from rag_engine import ask_question
import os

st.set_page_config(page_title="Assistente Inteligente de Entregas", layout="wide")

st.title("📦 Assistente Inteligente de Entregas")
st.write("Faça perguntas sobre a planilha Rel_Acomp_Entrega.csv")

# Upload da planilha
uploaded_file = st.file_uploader("Envie a planilha Rel_Acomp_Entrega.csv", type=["csv"])

if uploaded_file:
    st.success("Planilha carregada com sucesso!")

    # Salvar arquivo temporariamente
    with open("Rel_Acomp_Entrega.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.info("Processando a planilha...")

    db, df = load_data("Rel_Acomp_Entrega.csv")

    st.success("Base processada! Agora você pode conversar com a IA.")

    pergunta = st.text_input("Digite sua pergunta:")

    if st.button("Perguntar"):
        if pergunta.strip() == "":
            st.warning("Digite uma pergunta antes de enviar.")
        else:
            with st.spinner("Consultando dados..."):
                resposta = ask_question(db, pergunta)
            st.write("### 📌 Resposta:")
            st.write(resposta)
else:
    st.warning("Envie a planilha para começar.")
