import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# --- Load Environment Variables ---
load_dotenv()

# --- Streamlit UI ---
st.title("🎬 YouTube Video Assistant (RAG)")
video_id = st.text_input("Enter YouTube Video ID:", "Gfr50f6ZBvo")
user_question = st.text_input("Ask a question about the video:", "")

if st.button("Run Query") and video_id:
    try:
        # --- Ingest Transcript ---
        transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
        transcript = " ".join(chunk.text for chunk in transcript_list)

        # --- Split Transcript into Chunks ---
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.create_documents([transcript])

        # --- Embeddings + Vector Store ---
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_documents(chunks, embeddings)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        # --- LLM (HuggingFace) ---
        hf_llm = HuggingFaceEndpoint(
            repo_id="openai/gpt-oss-20b",
            task="text-generation"
        )
        llm = ChatHuggingFace(llm=hf_llm)

        # --- Prompt ---
        prompt = PromptTemplate(
            template="""
            You are a helpful assistant.
            Answer ONLY from the provided transcript context.
            If the context is insufficient, just say you don't know.

            Context:
            {context}

            Question: {question}
            """,
            input_variables=['context', 'question']
        )

        # --- Chain Assembly ---
        def format_docs(retrieved_docs):
            return "\n\n".join(doc.page_content for doc in retrieved_docs)

        parallel_chain = RunnableParallel({
            'context': retriever | RunnableLambda(format_docs),
            'question': RunnablePassthrough()
        })

        parser = StrOutputParser()
        main_chain = parallel_chain | prompt | llm | parser

        # --- Run Query ---
        if user_question.strip():
            st.subheader("Answer")
            answer = main_chain.invoke(user_question)
            st.write(answer)

    except TranscriptsDisabled:
        st.error("No captions available for this video.")
    except Exception as e:
        st.error(f"Error: {e}")
