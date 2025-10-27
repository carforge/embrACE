import sqlite3
from datetime import datetime

def log_interaction(user_input, agent_response):
    conn = sqlite3.connect("ace_data/context_traces.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS traces (
                    timestamp TEXT,
                    user_input TEXT,
                    agent_response TEXT
                )''')
    c.execute("INSERT INTO traces VALUES (?, ?, ?)", 
              (datetime.now().isoformat(), user_input, agent_response))
    conn.commit()
    conn.close()