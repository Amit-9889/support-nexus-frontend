import streamlit as st
from api import send_query, upload_document
from utils import init_session, add_messages, check_cache, update_cache

st.set_page_config(page_title="Support Nexus", layout="centered")

init_session()

st.title("Support Nexus")

# ===============================
# Sidebar → Upload Section
# ===============================

st.sidebar.header("📄 Upload Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    if st.sidebar.button("Upload"):
        with st.spinner("Uploading and processing..."):
            result = upload_document(uploaded_file)

        if result and result.get("status") == "success":
            st.sidebar.success("Document uploaded successfully")
        else:
            st.sidebar.error(
                f"Upload failed: {result.get('message') if result else 'Unknown error'}"
            )

# ===============================
# Main Chat Area
# ===============================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask question..."):

    add_messages("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    cached = check_cache(prompt)

    if cached:
        response = cached["response"]
        source = "From cache"
    else:
        with st.spinner("Thinking..."):
            response = send_query(prompt, st.session_state.user_id)
            update_cache(prompt, response)
        source = ""

    add_messages("assistant", response)

    with st.chat_message("assistant"):
        st.markdown(response)
        if source:
            st.caption(source)
