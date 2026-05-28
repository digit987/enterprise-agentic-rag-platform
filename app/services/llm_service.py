from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def generate_rag_response(
    query: str,
    context_chunks: list,
    history: list
):

    context = "\n\n".join(
        [chunk["text"] for chunk in context_chunks]
    )

    history_text = "\n".join([
        f"User: {item['user']}\nAssistant: {item['assistant']}"
        for item in history
    ])

    prompt = f"""
You are an enterprise AI assistant.

Use conversation history if relevant.

Answer ONLY using provided context.

Conversation History:
{history_text}

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful enterprise retrieval assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    output = response.choices[0].message.content

    usage = response.usage

    return {
        "answer": output,

        "usage": {
            "prompt_tokens": usage.prompt_tokens,
            "completion_tokens": usage.completion_tokens,
            "total_tokens": usage.total_tokens
        }
    }