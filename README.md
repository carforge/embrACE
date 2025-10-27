
# EmbrACE

**EmbrACE** (Agentic Context Engineering) is a modular, interactive application that combines LangChain, Streamlit, SQLite, and Tavily (for Web-Search) with a local Ollama instance. It enables dynamic agentic workflows with memory, tool augmentation, and context traceability.

---

## 🚀 Features

- 🔗 **LangChain Agent** with tool support and memory
- 🧠 **Context Memory** using LangChain's ConversationBufferMemory
- 🔍 **Web Search** via Tavily integration
- 🗃️ **Context Trace Logging** in SQLite
- 🖥️ **Streamlit UI** for interaction and visualization
- 🧩 Modular architecture for easy extension

---

## 🧱 Tech Stack

- **Python 3.10+**
- **LangChain**
- **Streamlit**
- **SQLite**
- **Tavily API** (for web search)
- **Ollama** (local LLM hosting Gemma 2:27B)

---

## 📁 Project Structure

```
ace-agent/
├── .env                      # API keys (e.g., TAVILY_API_KEY)
├── README.md
├── requirements.txt
├── main.py                   # Streamlit app entry point
│
├── ace_core/                 # Core ACE logic
│   ├── llm.py                # Ollama LLM setup
│   ├── memory.py             # LangChain memory setup
│   ├── tools.py              # Custom tools + Tavily search
│   └── agent.py              # Agent initialization
│
├── ace_data/                 # Data persistence
│   └── logger.py             # SQLite logging for context traces
│
├── ace_ui/                   # Streamlit UI components
│   └── layout.py             # Layout and visualization
│
└── ace_data_store/           # SQLite DB and other persistent files
    └── context_traces.db     # Auto-created
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/embrace.git
cd embrace
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
Create a `.env` file:
```
TAVILY_API_KEY=your-tavily-api-key
```

4. **Run the app**
```bash
streamlit run main.py
```

---

## 📌 Notes

- Context traces are stored in `ace_data_store/context_traces.db`

---

## 📄 License

MIT License

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
