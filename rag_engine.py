# rag_engine.py
from openai import OpenAI

# Cliente OpenAI (usa a variável de ambiente OPENAI_API_KEY do Streamlit secrets)
client = OpenAI()

def ask_question(db, pergunta, k=5):
    # busca documentos relevantes
    docs = db.similarity_search(pergunta, k=k)
    contexto = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
Você é um assistente especializado em análise de dados logísticos.
Responda APENAS com base nos dados abaixo (se não houver informação suficiente, diga que não encontrou dados).

DADOS:
{contexto}

PERGUNTA: {pergunta}
"""

    # chamada de chat
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )

    try:
        return resposta.choices[0].message["content"]
    except Exception:
        return getattr(resposta, "content", str(resposta))
