import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Enterprise Agentic RAG",
    layout="wide"
)

st.title("Enterprise Agentic RAG Platform")

st.subheader("Upload PDF")

uploaded_file = st.file_uploader(
    "Choose PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file,
            "application/pdf"
        )
    }

    if st.button("Upload"):

        response = requests.post(
            f"{BACKEND_URL}/api/v1/ingest/upload-pdf",
            files=files
        )

        st.json(response.json())

st.divider()

st.subheader("Chat")

session_id = st.text_input(
    "Session ID",
    value="demo_session"
)

query = st.text_area(
    "Ask a question"
)

if st.button("Submit Query"):

    payload = {
        "session_id": session_id,
        "query": query
    }

    response = requests.post(
        f"{BACKEND_URL}/api/v1/rag/chat",
        json=payload
    )

    result = response.json()

    st.markdown("### Response")

    st.write(result["response"])

    st.markdown("### Sources")

    for source in result["sources"]:

        st.expander(
            source["filename"]
        ).write(
            source["preview"]
        )