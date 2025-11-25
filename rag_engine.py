from openai import OpenAI
client = OpenAI()

def ask_question(db, pergunta):
    docs = db.similarity_search(pergunta, k=5)
    contexto = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Você é um assistente de logística e análise de entregas.
    Responda somente com base nos dados abaixo:

    {contexto}

    Pergunta: {pergunta}
    """

    resposta = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}]
    )

    return resposta.choices[0].message["content"]
