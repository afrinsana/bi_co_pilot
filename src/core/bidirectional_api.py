class BidirectionalAPI:
    def __init__(self):
        self.hcp_feedback = []
        self.mcp_feedback = []

    def log_hcp_feedback(self, feedback: str):
        self.hcp_feedback.append(feedback)

    def log_mcp_feedback(self, feedback: str):
        self.mcp_feedback.append(feedback)

    def get_insights(self):
        return {
            "human_feedback": self.hcp_feedback,
            "machine_feedback": self.mcp_feedback
        }