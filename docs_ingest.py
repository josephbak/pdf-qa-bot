
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from utils import GOOGLE_API_KEY

def load_and_embed_pdfs(pdf_folder: str, persist_path: str):
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
    all_docs = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(os.path.join(pdf_folder, filename))
            docs = loader.load()
            all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(all_docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(persist_path)
    print(f"Saved {len(chunks)} chunks to {persist_path}")

if __name__ == "__main__":
    load_and_embed_pdfs("data", "vector_store")
