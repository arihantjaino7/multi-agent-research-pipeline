# 🔍 Multi-Agent Research Pipeline

An autonomous AI research pipeline built with **LangGraph** and **LangChain** that takes any topic as input and generates a full structured research report — without any human intervention.

---

## 🚀 Demo

Give it a topic → it autonomously:

1. 🔎 **Searches the web** for the most relevant sources (Tavily Search API)
2. 📝 **Summarizes** each source using LLaMA 3.3 70B via Groq
3. 📄 **Writes a full research report** with Title, Executive Summary, Key Findings, and Conclusion
4. 💾 **Saves the report** as a `.md` file locally
5. 🖥️ **Serves a web UI** via Streamlit for easy interaction

---

## 🏗️ Architecture

```
User Input (Topic)
        ↓
  [LangGraph Pipeline]
        ↓
  ┌─────────────────────────────────┐
  │                                 │
[Search Node]               [Summarize Node]
 Tavily Web Search           LLM Summarization
        ↓                           ↓
                    [Report Node]
                  Final Report Generation
                           ↓
                      outputs/*.md
```

Each node is an independent agent that reads from and writes to a shared `ResearchState` object — passing data cleanly through the pipeline.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Agent Orchestration | LangGraph |
| LLM Framework | LangChain |
| LLM Model | LLaMA 3.3 70B via Groq |
| Web Search | Tavily Search API |
| UI | Streamlit |
| Package Manager | uv |

---

## 📁 Project Structure

```
research-pipeline/
│
├── agents/
│   ├── search_agent.py       # Web search tool using Tavily
│   ├── summarizer_agent.py   # Summarizes each source
│   └── report_writer.py      # Writes final research report
│
├── tools/
│   └── tavily_search.py      # Tavily API wrapper
│
├── graph/
│   └── pipeline.py           # LangGraph state graph
│
├── outputs/                  # Generated reports saved here
├── app.py                    # Streamlit web UI
├── main.py                   # CLI entry point
└── .env                      # API keys (not committed)
```

---

## ⚙️ Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/arihantjaino7/multi-agent-research-pipeline.git
cd multi-agent-research-pipeline
```

**2. Install dependencies**
```bash
uv venv
uv add langchain langchain-groq langgraph tavily-python python-dotenv streamlit
```

**3. Add API keys**

Create a `.env` file in the root:
```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

Get your keys:
- Groq → https://console.groq.com
- Tavily → https://tavily.com

---

## ▶️ Run

**CLI:**
```bash
uv run main.py
```

**Web UI:**
```bash
uv run streamlit run app.py
```

---

## 📄 Sample Output

**Input:** `"future of quantum computing"`

**Output:**
```
Title: The Future of Quantum Computing: Trends and Breakthroughs

Executive Summary:
Quantum computing is rapidly advancing beyond experimental stages...

Key Findings:
1. Hardware improvements in qubit stability...
2. Google and IBM racing toward fault-tolerant quantum systems...
3. Post-quantum cryptography becoming a national security priority...

Conclusion:
Quantum computing is expected to transform industries within the decade...
```

---

## 🔑 Key Concepts Used

- **LangGraph** — Stateful multi-agent orchestration with directed graphs
- **LangChain** — LLM chains, prompt templates, and tool calling
- **Groq** — Ultra-fast LLM inference using LLaMA 3.3 70B
- **Tavily** — Search API built specifically for AI agents
- **TypedDict State** — Shared state passed between all agents

---

## 🙋 Author

**Arihant Jain**
BTech CSE | Delhi
[GitHub](https://github.com/arihantjaino7)
