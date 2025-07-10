# app/rag_chain.py
import os
from dotenv import load_dotenv

from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()
os.environ['OPEN_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Load & split PDF
loader = PyPDFLoader('Cliead AI Knowledge Base.pdf')
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
documents = text_splitter.split_documents(docs)

# Embeddings & Vector Store
db = FAISS.from_documents(documents, OpenAIEmbeddings())

# LLM & Prompt
llm = ChatOpenAI(model="gpt-3.5-turbo")
prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context.
Think step by step before providing a detailed answer.
I will tip you $1000 if the user finds the answer helpful.
<context>
{context}                                          
</context>      
Question: {input}""")

document_chain = create_stuff_documents_chain(llm, prompt)
retriever = db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)


def run_rag_query(question: str) -> str:
    response = retrieval_chain.invoke({"input": question})
    return response['answer']
