import streamlit as st
from ace_core.agent import agent
from ace_data.logger import log_interaction
import sqlite3
import pandas as pd

st.set_page_config(page_title="EmbrACE", layout="wide")
st.title("🤖 EmbrACE – Agentic Context Engineering")

user_input = st.text_input("You:", "")

if user_input:
    response = agent.run(user_input)
    log_interaction(user_input, response)
    st.markdown(f"**Agent:** {response}")

    with sqlite3.connect("ace_data_store/context_traces.db") as conn:
        df = pd.read_sql_query("SELECT * FROM traces ORDER BY timestamp DESC", conn)
        st.subheader("🧠 Context Trace")
        st.dataframe(df)