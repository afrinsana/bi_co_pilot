import openai
from core.config import Config
from machine_copilot.error_handling import ErrorHandler

class OpenAIAdapter:
    def __init__(self):
        openai.api_key = Config.OPENAI_API_KEY

    @ErrorHandler.retry(max_attempts=3)
    def generate_text(self, prompt: str) -> str:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text