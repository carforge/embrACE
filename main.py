import streamlit as st
import sqlite3
import pandas as pd
from ace_core.agent import run_agent
from ace_data.logger import log_interaction

st.set_page_config(page_title="EmbrACE", layout="wide")
st.title("🤖 EmbrACE – Agentic Context Engineering")

# Ensure the table exists before querying
with sqlite3.connect("ace_data/context_traces.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS traces (
            timestamp TEXT,
            user_input TEXT,
            agent_response TEXT
        )
    ''')
    conn.commit()

    try:
        df = pd.read_sql_query("SELECT * FROM traces ORDER BY timestamp DESC", conn)
    except Exception:
        df = pd.DataFrame(columns=["user_input", "agent_response"])

# Display question-answer table
st.subheader("🧠 Conversation History")
st.table(df.rename(columns={
    'user_input': 'Question',
    'agent_response': 'Answer'
}))

# Input field below the table
st.subheader("💬 Ask EmbrACE")
user_input = st.text_area("Your question:", "", height=100)

if st.button("Submit") and user_input.strip():
    response = run_agent(user_input)
    log_interaction(user_input, response["messages"][-1].content)
    st.markdown(f"**Agent Response:** {response['messages'][-1].content}")
    st.markdown(f"Log: {response['messages']}")