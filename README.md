Local AI Knowledge Assistant

A personal project to learn and build a locally hosted AI assistant using open-source LLMs. The project will gradually expand to include RAG, MCP, AI agents and fine-tuning.

1. Prerequisites

- Windows 64-bit
- Python 3.13.14
- Ollama 0.40.17
- VS Code (recommended)

Ollama: https://ollama.com/download

2. Install and Configure Ollama

Install Ollama and download a lightweight model for local execution.

Command Prompt:

PS> ollama pull qwen3:1.7b

Verify the downloaded model:

PS> ollama list

Run the model:

PS> ollama run qwen3:1.7b

Check running models:

PS> ollama ps

Current model: Qwen3 1.7B
Execution: CPU

3. Project Setup

Create the project directory:

PS> mkdir C:\AI\local-ai-assistant
PS> cd C:\AI\local-ai-assistant
PS> mkdir backend
PS> cd backend

Create a Python virtual environment:

PS> python -m venv .venv

Activate it:

PS> .venv\Scripts\activate

4. Install Python Dependencies

Install the initial packages required for the backend:

(.venv) PS> pip install fastapi uvicorn ollama python-dotenv

Verify installed packages:

(.venv) PS> pip list

5. Current Project Structure

local-ai-assistant/
└── backend/
    └── .venv/
        ├── Include/
        ├── Lib/
        ├── Scripts/
        ├── .gitignore
        └── pyvenv.cfg

Application files such as "main.py" will be maintained outside ".venv".

---

Progress: Python environment configured, Ollama installed, Qwen3 1.7B downloaded, and initial backend dependencies installed.

More implementation steps and features will be documented as the project progresses.
