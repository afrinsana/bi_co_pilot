import os
import requests
from machine_copilot.error_handling import ErrorHandler
from core.config import Config

class TaskAutomator:
    @staticmethod
    @ErrorHandler.retry(max_attempts=3)
    def web_search(query: str) -> str:
        """Search the web using a mock API."""
        response = requests.get(
            "https://api.example.com/search",
            params={"q": query},
            headers={"Authorization": f"Bearer {Config.GITHUB_TOKEN}"}
        )
        return response.json().get("results", "No results found")

    @staticmethod
    def list_files(directory: str) -> list:
        """List files in a directory with error handling."""
        try:
            return os.listdir(directory)
        except Exception as e:
            ErrorHandler.log_errors(lambda: None)()  # Log the error
            return []