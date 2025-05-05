from typing import Dict
from machine_copilot.error_handling import ErrorHandler

class KnowledgeBase:
    def __init__(self):
        self._load_default_responses()

    def _load_default_responses(self) -> None:
        """Initialize with common Q&A pairs."""
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "goodbye": "Goodbye! Feel free to return if you have more questions.",
            "capabilities": "I can help with task automation, answer questions, and optimize machine learning models."
        }

    @ErrorHandler.log_errors
    def get_response(self, query: str) -> str:
        """Retrieve a pre-trained response or None if not found."""
        return self.responses.get(query.lower())

    def add_response(self, question: str, answer: str) -> None:
        """Dynamically add new Q&A pairs."""
        self.responses[question.lower()] = answer