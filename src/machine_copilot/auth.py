import keyring
from authlib.integrations.requests_client import OAuth2Session
from core.config import Config

class AuthManager:
    def __init__(self):
        self.oauth = OAuth2Session(
            client_id=Config.CLIENT_ID,
            client_secret=Config.CLIENT_SECRET,
            scope="read:user"
        )

    def save_token(self, service: str, token: str):
        """Store tokens securely."""
        keyring.set_password(service, "api_token", token)

    def get_token(self, service: str) -> str:
        """Retrieve tokens."""
        return keyring.get_password(service, "api_token")

    def github_oauth(self):
        """OAuth flow for GitHub."""
        authorization_url = self.oauth.create_authorization_url(
            "https://github.com/login/oauth/authorize"
        )
        print(f"Authorize here: {authorization_url}")
        token = self.oauth.fetch_token("https://github.com/login/oauth/access_token")
        self.save_token("github", token)
        return token

# Example usage:
# auth = AuthManager()
# auth.github_oauth()