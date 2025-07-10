# LangChain Q&A RAG App

A **local Retrieval-Augmented Generation (RAG) app** using **LangChain**, **FastAPI**, and **Uvicorn** to ask questions against your documents.

## 🚀 Features

- Upload and process your documents.
- Generate embeddings using OpenAI.
- Store and retrieve using FAISS vector store.
- Query using FastAPI endpoints.
- Serve locally with Uvicorn for API testing and frontend connection.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/langchain-qna-rag-app.git
   cd langchain-qna-rag-app
   ```

2. **Create and activate a virtual environment:**
```bash
conda create -n langenv310 python=3.10
conda activate langenv310
```

or using venv:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🏃 Running the App

Run the FastAPI app using Uvicorn:
```bash
uvicorn main:app --reload
```
Visit:
```bash
http://127.0.0.1:8000/docs
```
to test the API endpoints interactively.

## 📂 Project Structure
```css
Langchain-Q&A-RAG-App/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── app/
     ├── __init__.py
     ├── rag_chain.py
     └── api/
          ├── __init__.py
          └── app.py
```

## 🧩 Tech Stack

    LangChain
    FastAPI
    Uvicorn
    FAISS

## 🌱 Contributing

Feel free to fork, improve, and submit PRs.

## 📄 License

MIT (adjust if you choose a different license).

Happy building! 🚀