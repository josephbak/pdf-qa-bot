
import streamlit as st
from app import ask_question

st.title("📚 Ask Me Anything — PDF QA Bot")
query = st.text_input("Ask a question:")
if query:
    st.write("Thinking...")
    answer = ask_question(query, "./vector_store")
    st.write("**Answer:**", answer['result'])
