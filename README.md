# 📚 Ask Me Anything — PDF QA Bot

This is a simple RAG-based chatbot that lets you upload PDFs and ask questions about their content using Google's Gemini AI models.

## 🚀 Features
- Semantic search over PDF content using Google's embedding models
- Chunking + embeddings via FAISS vector store
- Source-aware answers from Gemini AI
- Streamlit UI (optional)

## 🛠️ Setup

```bash
git clone <repo>
cd pdf-qa-bot
pip install -r requirements.txt
```

Add your Google API key to `.env`:
```
GOOGLE_API_KEY=your-key
```

## 📂 Ingest PDFs

Place PDFs in `./data/` and run:

```bash
python docs_ingest.py
```

## 💬 Ask Questions

```bash
python -i app.py
ask_question("What is the main conclusion?", "vector_store")
```

or with UI:

```bash
streamlit run streamlit_app.py
```

## 🔧 Technical Details

- **LLM**: Google Gemini 1.5 Pro
- **Embeddings**: Google Generative AI Embeddings (models/embedding-001)
- **Vector Store**: FAISS
- **PDF Processing**: PyMuPDF
- **Text Splitting**: RecursiveCharacterTextSplitter (1000 chars, 200 overlap)