import streamlit as st
import sqlite3
import pandas as pd
from ace_core.agent import run_agent
from ace_data.logger import log_interaction

# Title
st.title("💬 Ask EmbrACE")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Your question..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run your local agent (Ollama)
    with st.chat_message("assistant"):
        response = run_agent(prompt)
        agent_reply = response["messages"][-1].content
        st.markdown(agent_reply)

    # Add agent response to history
    st.session_state.messages.append({"role": "assistant", "content": agent_reply})

    # Optional: log interaction
    log_interaction(prompt, agent_reply)