import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class Config:
    # Authentication
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    JWT_SECRET = os.getenv("JWT_SECRET", "default-secret-for-dev")
    
    # Monitoring
    PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", 8000))
    
    @staticmethod
    def validate():
        """Check required environment variables."""
        assert Config.OPENAI_API_KEY, "OPENAI_API_KEY not set in .env"