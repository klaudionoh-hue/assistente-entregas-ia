# load_csv.py
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def load_data(caminho_csv):
    # tenta ler com ';' e, se falhar, com ','
    try:
        df = pd.read_csv(caminho_csv, sep=';', encoding='latin1')
    except Exception:
        df = pd.read_csv(caminho_csv, sep=',', encoding='latin1')

    # converte todas as colunas para string e junta cada linha em um documento
    linhas_texto = df.astype(str).apply(lambda row: " | ".join(row.values), axis=1).tolist()

    # divide em pedaços (chunks) para indexação
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents(linhas_texto)

    # embeddings (modelo leve e rápido)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # cria base vetorial FAISS
    db = FAISS.from_documents(docs, embeddings)

    return db, df
