import streamlit as st


def init_session():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "cache" not in st.session_state:
        st.session_state.cache = {}

    if "user_id" not in st.session_state:
        st.session_state.user_id = "Amit_123"


def add_messages(role,content):
    st.session_state.messages.append({
        "role":role,
        "content":content
    })


def check_cache(question):
    return st.session_state.cache.get(question)


def update_cache(question,response):
    if question in st.session_state.cache:
        st.session_state.cache[question]["count"]+=1

    else:
        st.session_state.cache[question]=({
            "response":response,
            "count":1
        })