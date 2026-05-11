from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


def generate_answer(question: str, context_chunks: list[str]) -> str:

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Error: GEMINI_API_KEY not found"

    try:
        client = genai.Client(api_key=api_key)

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

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini failed: {str(e)}"
