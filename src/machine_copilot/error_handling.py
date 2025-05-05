import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from core.config import Config

logging.basicConfig(filename="mcp_errors.log", level=logging.ERROR)

class ErrorHandler:
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True
    )
    def api_call(self, func, *args, **kwargs):
        """Retry failed API calls with exponential backoff."""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"API call failed: {e}")
            raise

    def fallback_model(self, model, backup_model):
        """Switch to a backup model if primary fails."""
        try:
            return model.predict()
        except Exception as e:
            logging.warning(f"Fallback triggered: {e}")
            return backup_model.predict()

# Example usage:
# handler = ErrorHandler()
# handler.api_call(risky_function, arg1, arg2)