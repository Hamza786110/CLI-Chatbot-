#  CLI Chatbot

A simple terminal-based chatbot built with **LangChain**, **LangGraph**, and **Groq**. Chat directly from your terminal with memory support per user session.

---

## Features

-  Conversational AI in your terminal
-  Memory support per user session via LangGraph
-  Powered by Qwen3-32B via Groq
-  Secure API key management with `.env`

---

## 🛠️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create a virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file in the root directory and add:
```
GROQ_API_KEY=your_api_key_here
```

> Get your free API key from [https://console.groq.com](https://console.groq.com)

---

## Run

```bash
python CLI_chatbot.py
```

---

## 💬 Usage

- Enter your name when prompted — this creates a unique session for you
- Type your query and press **Enter** to chat
- Press **Enter** on an empty input to **exit**

---

## Project Structure

```
├── CLI_chatbot.py      # Main chatbot script
├── .env                # Your API keys (never push this!)
├── .gitignore          # Files to exclude from Git
└── requirements.txt    # Python dependencies
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [LangChain](https://langchain.com) | Agent framework |
| [LangGraph](https://langchain-ai.github.io/langgraph) | Memory & state management |
| [Groq](https://groq.com) | LLM inference (Qwen3-32B) |
| [Python](https://python.org) | Core language |

---

## Important

Never push your `.env` file to GitHub. Make sure your `.gitignore` includes:
```
.env
venv/
__pycache__/
```

---
