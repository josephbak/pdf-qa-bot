from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from utils import GOOGLE_API_KEY
import os

def ask_question(query: str, persist_path: str):
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    db = FAISS.load_local(persist_path, GoogleGenerativeAIEmbeddings(model="models/embedding-001"), allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    result = qa(query)
    print("Answer:", result['result'])
    print("\nSources:")
    for doc in result['source_documents']:
        print(" -", doc.metadata.get("source", "unknown"))

    return result
