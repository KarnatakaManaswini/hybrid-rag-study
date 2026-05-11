'''from openai import OpenAI
import os


def get_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found")
    return OpenAI(api_key=api_key)


def generate_answer(question: str, context_chunks: list[str]) -> str:
    client = get_client()

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful study assistant.
Answer the question using ONLY the context below.
If the answer is not present, say "Answer not found in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()




'''
import google.generativeai as genai
import os


def generate_answer(question: str, context_chunks: list[str]) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Error: GEMINI_API_KEY not found"

    genai.configure(api_key=api_key)

    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a helpful study assistant.
Answer the question using ONLY the context below.

If the answer is not present, say:
"Answer not found in the document"

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if response.text:
            return response.text.strip()
        return "No response generated."

    except Exception as e:
        return f"Gemini failed: {str(e)}"
    

    
