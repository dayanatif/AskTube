# 🎬 AskTube  
An AI-powered assistant that lets you **chat with YouTube videos** using **RAG (Retrieval-Augmented Generation)**.  
AskTube helps you **ask questions, get summaries, and explore transcripts** — powered by **LangChain, FAISS, HuggingFace, and Google Generative AI embeddings**.  

---

## 🚀 Features  
✅ Automatically fetches **YouTube transcripts**  
✅ Splits transcripts into chunks & embeds with **FAISS**  
✅ Uses **Google Generative AI embeddings** for semantic search  
✅ **HuggingFace LLMs** provide intelligent answers  
✅ **Streamlit UI** for interactive Q&A  
✅ **Deployment-ready** on Streamlit Cloud  

---

## 📦 Installation  

### 1. Clone the repo  
```bash
git clone https://github.com/dayanatif/AskTube.git
cd AskTube

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

streamlit run app.py

