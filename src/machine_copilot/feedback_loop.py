from core.bidirectional_api import BidirectionalAPI
from core.config import Config
from datetime import datetime
import numpy as np

class FeedbackLoop:
    def __init__(self):
        self.api = BidirectionalAPI()

    def send_to_mcp(self, feedback: str):
        """HCP sends feedback to MCP (e.g., 'model is too slow')."""
        self.api.log_hcp_feedback(feedback)
        print(f"Feedback sent: {feedback}")

    def apply_mcp_insights(self):
        """MCP adjusts based on HCP feedback."""
        insights = self.api.get_insights()
        for feedback in insights["human_feedback"]:
            if "slow" in feedback:
                print("MCP: Optimizing model speed...")
                # Add logic to reduce model complexity
    def __init__(self):
        self.metrics = []  # Stores performance data

    def log_metrics(self, latency: float, accuracy: float):
        """Track model performance over time."""
        self.metrics.append({
            "timestamp": datetime.now(),
            "latency": latency,
            "accuracy": accuracy
        })

    def suggest_hcp_improvements(self):
        """MCP recommends HCP enhancements."""
        avg_latency = np.mean([m["latency"] for m in self.metrics])
        if avg_latency > 0.5:
            return "HCP: Simplify user queries to reduce model load"
        return None

# Example usage:
# loop = FeedbackLoop()
# loop.send_to_mcp("Model is too slow")
# loop.apply_mcp_insights()