import uuid
from dotenv import load_dotenv

import chromadb
import streamlit as st
from sentence_transformers import SentenceTransformer

load_dotenv()

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

client = chromadb.Client()
# collection = client.get_or_create_collection(name="knowledge_base")

def get_collection():
    if "collection_name" not in st.session_state:
        st.session_state["collection_name"] = f"kb_{uuid.uuid4().hex}"
    return client.get_or_create_collection(name=st.session_state["collection_name"])

def add_to_knowledge_base(chunks):
    
    model = load_model()

    embeddings = model.encode(chunks).tolist()

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection = get_collection()

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

def search_knowledge_base(query):

    model = load_model()

    query_embedding = model.encode(query).tolist()

    collection = get_collection()

    search_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    return search_results["documents"][0]

def reset_knowledge_base():
    if "collection_name" in st.session_state:
        try:
            client.delete_collection(st.session_state["collection_name"])
        except Exception:
            pass
        del st.session_state["collection_name"]