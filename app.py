# app.py
import streamlit as st
from load_csv import load_data
from rag_engine import ask_question

st.set_page_config(page_title="Assistente Inteligente de Entregas", layout="wide")
st.title("📦 Assistente Inteligente de Entregas")
st.write("Envie a planilha Rel_Acomp_Entrega.csv e faça perguntas sobre os dados.")

uploaded_file = st.file_uploader("Envie a planilha (CSV)", type=["csv"])
if uploaded_file:
    # salva temporariamente
    with open("Rel_Acomp_Entrega.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Planilha salva. Processando... (pode levar alguns segundos)")
    try:
        db, df = load_data("Rel_Acomp_Entrega.csv")
        st.success("Base processada! Você pode fazer perguntas agora.")
    except Exception as e:
        st.error(f"Erro ao processar a planilha: {e}")
        st.stop()

    pergunta = st.text_input("Digite sua pergunta sobre a base")
    if st.button("Perguntar"):
        if pergunta.strip() == "":
            st.warning("Digite uma pergunta.")
        else:
            with st.spinner("Consultando IA..."):
                try:
                    resposta = ask_question(db, pergunta)
                    st.write("### Resposta")
                    st.write(resposta)
                except Exception as e:
                    st.error(f"Erro ao consultar a IA: {e}")
else:
    st.info("Faça upload da planilha para começar.")
