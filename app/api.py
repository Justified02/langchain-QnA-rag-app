# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from .rag_chain import run_rag_query


app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QueryRequest):
    answer = run_rag_query(request.question)
    return {"answer": answer}
