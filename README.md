# 🤖 KL University RAG-based Assistant

This is a **Streamlit-powered RAG (Retrieval-Augmented Generation) assistant** built for answering questions related to KL University. It uses semantic search with `sentence-transformers` and generates answers with Hugging Face's `Qwen2.5-72B-Instruct` model.

---

## 🚀 Features

- 🔍 Semantic context retrieval from `Text_File.txt`
- 🧠 LLM-powered answer generation using Hugging Face Inference API
- 💬 User-friendly web UI with Streamlit
- 🔐 Secure API key handling via `.env`

---

## 🧱 Project Structure

rag-based-assistant/

├── app.py # Streamlit app

├── Text_File.txt # Source document for QA

├── .gitignore # Files to ignore

├── requirements.txt # Required packages

└── README.md # Project documentation


---

### ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/Vidhyadhar75/rag-based-assistant.git
cd rag-based-assistant
```
## 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---

### 🔐 Setup .env File

Create a .env file in the root folder:

```env
HF_API_KEY=your_huggingface_api_key
```
Make sure .env is listed in .gitignore to keep your key private.

## ▶️ Run the App
```bash
streamlit run app.py
```
Visit http://localhost:8501 in your browser.

## 🧠 Models Used
| Component       | Model Used                                       |
| --------------- | ------------------------------------------------ |
| Embeddings      | `sentence-transformers/all-MiniLM-l6-v2`         |
| Text Generation | `Qwen/Qwen2.5-72B-Instruct` via Hugging Face API |


## 📝 Example Usage
Add your data to Text_File.txt (separate logical sections with \n\n).

Run the app and type a query like:

```pgsql
What is the dress code policy at KL University?
```
The app will:

Embed your query

Retrieve the top 2 semantically similar chunks

Prompt the LLM with context

Display the generated answer

## 🛡️ Security Notice
✅ API Key is loaded securely using python-dotenv.
❌ Never hardcode your Hugging Face API key into your Python script.



## 👤 Author
Vidhyadhara Rao Kotagiri

🎓 B.Tech IoT | KL University

🌐 GitHub | LinkedIn
