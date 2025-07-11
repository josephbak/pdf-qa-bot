
# 📚 Ask Me Anything — PDF QA Bot

This is a simple RAG-based chatbot that lets you upload PDFs and ask questions about their content using OpenAI's GPT models.

## 🚀 Features
- Semantic search over PDF content
- Chunking + embeddings via FAISS
- Source-aware answers from LLM
- Streamlit UI (optional)

## 🛠️ Setup

```bash
git clone <repo>
cd pdf-qa-bot
pip install -r requirements.txt
```

Add your OpenAI key to `.env`:
```
OPENAI_API_KEY=your-key
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
