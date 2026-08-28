import os

import streamlit as st

from pdf_processor import (extract_text, chunk_text)
from vector_store import (add_to_knowledge_base, search_knowledge_base, reset_knowledge_base)
from prompts import build_prompt
from groq_client import ask_llm

st.set_page_config(page_title="PDF Chat Assistant", layout="wide")
st.title("PDF Chat Assistant")
st.caption("Transform any PDF into an interactive conversation.")

with st.sidebar:
    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"],
        help="Supported format: PDF(.pdf)"
    )

    if uploaded_file:
        file_name = os.path.splitext(uploaded_file.name)[0]
        st.success(f"{file_name}")

    if uploaded_file and "db_ready" not in st.session_state:

        try:
            with st.spinner("Processing PDF...."):
                text = extract_text(uploaded_file)

                if text.strip() == "":
                    st.warning("This PDF contains no extractable text. It may be a scanned/image-only PDF.")
                    st.stop()

                chunks = chunk_text(text, 300, 75)

                add_to_knowledge_base(chunks)

                st.session_state["db_ready"] = True

        except Exception as e:
            st.error(f"Error: {e}")

    if st.session_state.get("db_ready"):
        if st.button("Start Over / Upload New PDF"):
            reset_knowledge_base()
            st.session_state.clear()
            st.rerun()

# conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_search = st.chat_input("Ask your question...")

if user_search:

    st.session_state["messages"].append({"role": "user", "content":user_search})

    with st.chat_message("user"):
        st.write(user_search)

    if st.session_state.get("db_ready", False):

        try:
            context = search_knowledge_base(user_search)

            prompt = build_prompt(context, user_search)

            reply = ask_llm(prompt)

            with st.chat_message("assistant"):
                full_reply = st.write_stream(reply)

                st.session_state["messages"].append({"role":"assistant", "content":full_reply})
                
        except Exception as e:
            with st.chat_message("assistant"):
                st.error(f"Something went wrong while generating a response: {e}")
    else:
        with st.chat_message("assistant"):
            st.write("Please upload a PDF first.")