Local AI Knowledge Assistant

A personal project to explore and build a locally hosted AI assistant using open-source Large Language Models (LLMs). The project will gradually expand to include RAG, MCP, AI agents, and fine-tuning.

Tech Stack

- Python 3.13
- Ollama
- Qwen3 1.7B
- FastAPI
- Uvicorn

Setup Completed

1. Install Python

- Installed Python 3.13.14.
- Verified installation:

python --version

2. Install Ollama

- Installed Ollama for Windows.
- Download: https://ollama.com/download
- Verified installation:

ollama --version

3. Download Local LLM

- Downloaded the Qwen3 1.7B model.

ollama pull qwen3:1.7b

- Verified downloaded models:

ollama list

4. Create Python Virtual Environment

Created the project structure:

local-ai-assistant/
└── backend/
    └── .venv/

Created and activated the virtual environment:

python -m venv .venv
.venv\Scripts\activate

5. Install Python Dependencies

Installed the initial backend dependencies:

pip install fastapi uvicorn ollama python-dotenv

Verified installed packages:

pip list

Current Project Structure

local-ai-assistant/
└── backend/
    ├── .venv/
    ├── main.py
    └── requirements.txt

Next Steps

- Build FastAPI endpoints for local LLM interaction.
- Connect FastAPI with Ollama.
- Add conversation history and streaming responses.
- Gradually introduce RAG, MCP, AI agents, and fine-tuning.
