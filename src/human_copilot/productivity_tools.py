import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from github import Github

class ProductivityTools:
    def __init__(self):
        self.calendar_service = self._init_calendar()
        self.github_client = Github(os.getenv("GITHUB_TOKEN"))

    def _init_calendar(self):
        """Authenticate with Google Calendar."""
        creds = service_account.Credentials.from_service_account_file(
            "credentials.json", scopes=["https://www.googleapis.com/auth/calendar"]
        )
        return build("calendar", "v3", credentials=creds)

    def get_upcoming_events(self, max_results=5):
        """Fetch calendar events."""
        events = self.calendar_service.events().list(
            calendarId="primary", maxResults=max_results
        ).execute()
        return events.get("items", [])

    def create_github_issue(self, repo_name: str, title: str, body: str):
        """Create a GitHub issue."""
        repo = self.github_client.get_repo(repo_name)
        repo.create_issue(title=title, body=body)

# Example usage:
# tools = ProductivityTools()
# tools.get_upcoming_events()
# tools.create_github_issue("user/repo", "Bug", "Fix this!")