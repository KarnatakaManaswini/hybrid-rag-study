I built a RAG-based AI Study Assistant that allows users to upload a PDF and ask questions, and the system answers strictly based on the content of that document.

I implemented a complete RAG pipeline—from document ingestion to retrieval and context-aware answer generation using an LLM.
When a user uploads a PDF, the system first extracts all the text using a PDF parsing library. Since the extracted content can be large and unstructured, I split it into smaller chunks. Each chunk contains a few hundred words, and I allowed a small overlap between chunks so that we don’t lose any context at the boundaries.

Once the document is converted into chunks, I build a retrieval system on top of it. I used a TF-IDF–based local retriever, where each chunk is converted into a vector representing word importance.

Now, when the user asks a question, the query is also converted into a vector and compared with all the chunk vectors using cosine similarity. Based on this, the system retrieves the most relevant chunks instead of using the entire document.
These relevant chunks are then passed to a language model along with the user’s question.

I used Google Gemini’s 2.5 Flash model for answer generation. This is where the RAG concept comes in—only the retrieved context is given to the model, not the full document.

I also designed the prompt in such a way that the model answers only from the given context, and if the answer is not present, it clearly says so. This helps reduce hallucination and improves reliability.

Finally, I integrated everything into a Streamlit interface, where users can upload a PDF once and interact with it by asking multiple questions.
