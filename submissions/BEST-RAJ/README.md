# RAG Chat Pilot

A Retrieval-Augmented Generation (RAG) application that lets you upload a PDF and have a grounded, context-aware conversation with its contents. Built as a reference implementation for a hands-on RAG workshop — clean, minimal, and structured for learning.

**Live demo:** [rag-chat-pilot.streamlit.app](https://rag-chat-pilot.streamlit.app) *(replace with your actual Streamlit Cloud URL)*

---

## What it does

Upload any text-based PDF, and RAG Chat Pilot will:

1. Extract and chunk the document's text
2. Generate embeddings for each chunk using a local sentence-transformer model
3. Store those embeddings in a vector database (ChromaDB)
4. Retrieve the most relevant chunks for each question you ask
5. Pass that context to an LLM (via Groq) to generate a grounded, accurate answer

The assistant answers **only** from the uploaded document's content — no hallucinated facts, no outside knowledge — while still handling greetings and small talk naturally.

---

## Tech stack

| Layer | Tool |
|---|---|
| UI | [Streamlit](https://streamlit.io/) |
| PDF parsing | [pypdf](https://pypi.org/project/pypdf/) |
| Embeddings | [sentence-transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`) |
| Vector store | [ChromaDB](https://www.trychroma.com/) |
| LLM | [Groq](https://groq.com/) (`llama-3.3-70b-versatile`) |

---

## Project structure

```
rag-chat-pilot/
├── app.py              # Streamlit UI and main app flow
├── pdf_processor.py     # PDF text extraction and chunking
├── vector_store.py       # Embedding generation, ChromaDB storage and search
├── prompts.py            # Prompt template for grounded Q&A
├── groq_client.py        # Groq API client and streaming response handler
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/rag-chat-pilot.git
cd rag-chat-pilot
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the example file and fill in your keys:

```bash
cp .env.example .env
```

Edit `.env`:

```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

- **GROQ_API_KEY** — get a free key at [console.groq.com](https://console.groq.com)
- **HF_TOKEN** — get a free **Read-only** token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (used only to download the embedding model with higher rate limits; the app works without it too, just slower on first run)

### 5. Pre-download the embedding model (recommended)

This avoids a ~30-40 second delay the first time you upload a PDF:

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

### 6. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## How it works (for workshop attendees)

This project demonstrates the core RAG pipeline end-to-end:

**Chunking** — `pdf_processor.py` splits extracted text into overlapping character-based chunks (`chunk_size=300`, `overlap=75`). This is the simplest possible chunking strategy — production systems typically use token-aware or sentence-aware splitting instead.

**Embedding** — `vector_store.py` uses `sentence-transformers` to convert each chunk into a vector representation, run locally (no external API call per chunk).

**Storage & retrieval** — ChromaDB stores the embeddings and handles similarity search. Each user session gets its own isolated collection, so multiple people using the app (or testing locally) don't see each other's documents.

**Augmentation** — `prompts.py` builds a strict prompt instructing the LLM to answer only from retrieved context, reducing hallucination.

**Generation** — `groq_client.py` streams the LLM's response back to the UI token-by-token via Groq's fast inference API.

---

## Known limitations

This is a **basic** RAG implementation, intentionally kept simple for teaching purposes. A few things it does *not* do, by design:

- No multi-turn conversational memory — each question is answered independently from retrieved context, not previous chat turns
- Chunking is character-based, not sentence- or token-aware
- No persistent storage — the knowledge base resets when the app restarts (in-memory ChromaDB client)
- No support for scanned/image-only PDFs (no OCR)
- Uploading a new PDF replaces the current session's knowledge base; it doesn't merge with a previous upload

These are good next steps if you want to extend the project after the workshop.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

Built for a community RAG workshop to demonstrate the fundamentals of Retrieval-Augmented Generation using open, freely available tools.
