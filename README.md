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

```bash
# 1. Clone the repository
git clone https://github.com/dayanatif/AskTube.git
cd AskTube

# 2. Create virtual environment
python -m venv venv

# Activate venv
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (create a .env file instead for persistence)
export GOOGLE_API_KEY=your_google_api_key
export HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token

# On Windows (PowerShell):
# $env:GOOGLE_API_KEY="your_google_api_key"
# $env:HUGGINGFACEHUB_API_TOKEN="your_huggingface_api_token"

# 5. Run the Streamlit app
streamlit run app.py

