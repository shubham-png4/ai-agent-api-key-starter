import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class SimpleAIAgent:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is missing")
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    def respond(self, user_input: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=user_input,
        )
        return response.output_text