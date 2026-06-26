# ai-agent-api-key-starter

A minimal, GitHub-ready Python starter for building an AI agent that uses an API key from environment variables.

## Repository name
`ai-agent-api-key-starter`

## Description
A simple starter project for an AI agent that loads its API key from `.env`, sends a prompt to an LLM provider, and returns a response.

## Project structure
```text
ai-agent-api-key-starter/
├── codes/
│   ├── main.py
│   ├── agent.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
└── README.md
```

## Setup
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r codes/requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your API key.
4. Run the agent:
   ```bash
   python codes/main.py
   ```

## Environment variables
- `OPENAI_API_KEY` — your API key.
- `OPENAI_MODEL` — optional model name.

## Notes
- Do not commit your real API key.
- Keep `.env` out of GitHub.
- This starter uses a simple command-line loop that you can extend into a real multi-step agent.