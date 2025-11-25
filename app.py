import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

def load_data(caminho_csv):
    # Carrega o CSV
    df = pd.read_csv(caminho_csv, sep=";", encoding="latin1")

    # Concatena todas as linhas em texto legível
    linhas_texto = df.astype(str).apply(lambda row: " | ".join(row.values), axis=1).tolist()

    # Divide o texto em pedaços
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents(linhas_texto)

    # Cria embeddings
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Cria base vetorial FAISS
    db = FAISS.from_documents(docs, embeddings)

    return db, df
