python -m venv venv


venv\Scripts\activate

pip install -r requirements.txt


streamlit run app.py

GEMINI_API_KEY=


I built a RAG-based AI Study Assistant that allows users to upload a PDF and ask questions, and the system answers strictly based on the content of that document.
The project follows a complete RAG pipeline.
When a user uploads a PDF, the system first extracts all the text using a PDF parsing library. Since the extracted content can be large and unstructured, I split it into smaller chunks. Each chunk contains a few hundred words, and I maintain a small overlap between chunks to preserve context across boundaries.
Once the document is converted into chunks, I build a retrieval system on top of it. I used a TF-IDF–based local retriever, where each chunk is converted into a vector representing word importance.
Now, when the user asks a question, the query is also converted into a vector and compared with all the chunk vectors using cosine similarity. Based on this, the system retrieves the most relevant chunks instead of using the entire document.
These relevant chunks are then passed to a language model along with the user’s question. I used Google’s Gemini model for answer generation. This is where the RAG concept comes in—only the retrieved context is given to the model, not the full document.
I also designed the prompt in such a way that the model answers only from the given context, and if the answer is not present, it clearly says so. This helps reduce hallucination and improves reliability.
Finally, I integrated everything into a Streamlit interface, where users can upload a PDF once and interact with it by asking multiple questions.
