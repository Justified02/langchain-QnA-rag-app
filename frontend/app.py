# frontend/app.py
import requests
import streamlit as st

st.title("📚 Cliead AI RAG Q&A Chatbot")

question = st.text_input("Ask your question:")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": question}
        )
        answer = response.json().get("answer", "No answer returned.")
        st.write("### Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
