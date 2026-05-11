from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import tempfile

from src.ingestion.pdf_loader import load_pdf_text
from src.ingestion.chunker import chunk_text
from src.retriever.local_retriever import LocalRetriever
from src.qa.rag_chat import generate_answer

st.set_page_config(page_title="Hybrid RAG Study Chatbot", layout="wide")
st.title("📘 Hybrid RAG Study Chatbot")

# Session state
if "retriever" not in st.session_state:
    st.session_state.retriever = None

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and st.session_state.retriever is None:
    with st.spinner("Processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        text = load_pdf_text(pdf_path)
        chunks = chunk_text(text)

        # filter + limit
        chunks = [c for c in chunks if len(c.strip()) > 50][:20]

        st.session_state.retriever = LocalRetriever(chunks)

    st.success("PDF processed successfully ✅")

# Ask question
question = st.text_input("Ask a question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif st.session_state.retriever is None:
        st.warning("Upload a PDF first.")
    else:
        with st.spinner("Thinking..."):
            context = st.session_state.retriever.retrieve(question)
            answer = generate_answer(question, context)

        st.subheader("Answer")
        st.write(answer)
