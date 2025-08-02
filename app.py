import streamlit as st
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()


# Load sentence transformer
sent_transformer = SentenceTransformer('sentence-transformers/all-MiniLM-l6-v2')

# Load and chunk data
@st.cache_data
def load_data():
    with open("Text_File.txt", "r", encoding="utf-8") as file:
        chunks = file.read().split("\n\n")
    return {tuple(sent_transformer.encode(chunk)): chunk for chunk in chunks if chunk.strip()}

encoded_chunks = load_data()

# Initialize Hugging Face Inference Client with API key in code
client = InferenceClient(api_key=os.environ["HF_API_KEY"])


# Context retrieval
def find_relevant_context(query):
    query_vec = sent_transformer.encode(query)
    scores = [
        (chunk, np.dot(query_vec, np.array(embed)) /
         (np.linalg.norm(query_vec) * np.linalg.norm(embed)))
        for embed, chunk in encoded_chunks.items()
    ]
    scores.sort(key=lambda x: x[1], reverse=True)
    return " ".join(scores[i][0] for i in range(min(2, len(scores))))

# Query answering
def answer_question(query):
    context = find_relevant_context(query)
    prompt = f"CONTEXT: {context}\nQUESTION: {query}\nAnswer the question in under 50 words."
    messages = [{"role": "user", "content": prompt}]

    stream = client.chat.completions.create(
        model="Qwen/Qwen2.5-72B-Instruct",
        messages=messages,
        temperature=0.7,
        max_tokens=256,
        top_p=0.7,
        stream=True
    )

    response = ''.join(chunk.choices[0].delta.content or '' for chunk in stream)
    return response

# Streamlit UI
st.set_page_config(page_title="KL University Assistant", layout="centered")
st.title("📘 KL University Assistant (RAG-based QA)")
st.write("Ask any question based on the document content.")

query = st.text_input("Enter your question:")
if query:
    with st.spinner("Generating answer..."):
        try:
            answer = answer_question(query)
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
