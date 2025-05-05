import sys
sys.path.append("src")

#!/usr/bin/env python3
"""
Bi-Co-Pilot - Advanced Main Entry Point
Integrates Human Co-Pilot (HCP) and Machine Co-Pilot (MCP) with:
1. Voice/Text interfaces
2. AutoML model optimization
3. Secure OAuth authentication
4. Robust error handling
5. Bidirectional feedback loops
"""

import torch
import torch.nn as nn
from src.human_copilot import HumanCoPilot
from src.machine_copilot import ModelOptimizer, AuthManager, FeedbackLoop
from machine_copilot.error_handling import ErrorHandler
from core.config import Config

def setup_environment():
    """Initialize configuration and environment checks."""
    Config.validate()  # Checks if required API keys exist
    print("✓ Environment configured")

def demo_hcp():
    """Run Human Co-Pilot with voice/text interaction."""
    hcp = HumanCoPilot()
    print("\n=== Human Co-Pilot Demo ===")
    hcp.run(
        mode="voice",  # Try "text" for CLI input
        task="schedule meeting with team at 3pm tomorrow"
    )

def demo_mcp():
    """Run Machine Co-Pilot with model optimization."""
    print("\n=== Machine Co-Pilot Demo ===")
    
    # 1. Model Optimization
    model = nn.Sequential(
        nn.Linear(10, 50),
        nn.ReLU(),
        nn.Linear(50, 2)
    )
    optimizer = ModelOptimizer(model)
    
    # AutoML Hyperparameter Tuning
    study = optimizer.tune_hyperparameters(
        direction="minimize",
        n_trials=10,
        dataset=torch.randn(100, 10)  # Mock data
    )
    print(f"Best model params: {study.best_params}")
    
    # Model Pruning
    optimizer.prune_model(amount=0.2)

    # 2. Secure Authentication
    auth = AuthManager()
    if not auth.get_token("github"):
        auth.github_oauth()
    print("✓ GitHub authentication complete")

def run_feedback_loop():
    """Demonstrate HCP-MCP bidirectional learning."""
    print("\n=== Feedback Loop Demo ===")
    feedback = FeedbackLoop()
    
    # HCP reports issue to MCP
    feedback.send_to_mcp(
        "Model predictions are 20% slower than acceptable"
    )
    
    # MCP responds to feedback
    feedback.apply_mcp_insights()  # Triggers optimization

def main():
    try:
        # Initialize
        setup_environment()
        ErrorHandler.setup_logging()
        
        # Run Demos
        demo_hcp()
        demo_mcp()
        run_feedback_loop()
        
    except Exception as e:
        ErrorHandler.critical_shutdown(e)

if __name__ == "__main__":
    main()