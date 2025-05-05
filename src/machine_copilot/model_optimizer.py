import optuna
import torch
import torch.nn as nn
import torch_pruning as pruning

class ModelOptimizer:
    def __init__(self, model: nn.Module):
        self.model = model

    def optimize_hyperparams(self, trial: optuna.Trial, train_loader) -> float:
        """AutoML: Optimize learning rate and batch size."""
        lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        
        # Training loop (simplified)
        for epoch in range(5):
            for batch in train_loader:
                optimizer.zero_grad()
                loss = self.model(batch).mean()
                loss.backward()
                optimizer.step()
        return loss.item()

    def prune_model(self, amount=0.3):
        """Remove 30% of least important model weights."""
        pruner = pruning.MagnitudePruner(self.model)
        pruner.prune(amount=amount)
        print(f"Pruned {amount*100}% of weights.")

# Example usage:
# study = optuna.create_study(direction="minimize")
# study.optimize(lambda trial: optimizer.optimize_hyperparams(trial, train_loader), n_trials=10)
# optimizer.prune_model(amount=0.2)