import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def load_data(csv_path):
    df = pd.read_csv(csv_path, sep=';')

    # Transformar cada linha em texto único
    documentos = []
    for i, row in df.iterrows():
        texto = " | ".join([f"{col}: {row[col]}" for col in df.columns])
        documentos.append(texto)

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=50)
    chunks = splitter.split_text("\n".join(documentos))

    embeddings = OpenAIEmbeddings()
    db = Chroma.from_texts(chunks, embeddings)

    return db, df
