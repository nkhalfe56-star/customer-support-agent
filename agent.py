from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Customer Support Agent API", version="1.0")

# ── Config ─────────────────────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
KB_PATH = "data/knowledge_base.txt"
MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.2
MEMORY_WINDOW = 5

SYSTEM_PROMPT = """You are a helpful customer support agent for an e-commerce platform.
Always be polite, concise, and factual. If you don't know the answer, say so clearly
and offer to escalate to a human agent. Use the provided knowledge base context first."""


# ── Knowledge Base Setup ─────────────────────────────────────────────────────
def build_vectorstore(kb_path: str) -> FAISS:
    loader = TextLoader(kb_path, encoding="utf-8")
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


# ── Agent Setup ─────────────────────────────────────────────────────────────
vectorstore = build_vectorstore(KB_PATH)

llm = ChatOpenAI(
    model_name=MODEL,
    temperature=TEMPERATURE,
    openai_api_key=OPENAI_API_KEY,
)

memory = ConversationBufferWindowMemory(
    k=MEMORY_WINDOW,
    memory_key="chat_history",
    return_messages=True,
    output_key="answer",
)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    memory=memory,
    return_source_documents=False,
    verbose=False,
)


# ── API Models ─────────────────────────────────────────────────────────────
class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    answer: str
    session_id: str


# ── Routes ────────────────────────────────────────────────────────────────────
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = chain({"question": req.message})
    return ChatResponse(answer=result["answer"], session_id=req.session_id)


@app.delete("/session/{session_id}")
def clear_session(session_id: str):
    memory.clear()
    return {"message": f"Session {session_id} cleared"}


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
