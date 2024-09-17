# Import dependencies
import os
import wandb
import wandb_workspaces.workspaces as ws
import wandb_workspaces.reports.v2 as wr 

# Initialize Weights & Biases and Login
wandb.login()

# Function to create a new project and log sample data
def create_project_and_log_data():
    project = "workspace-api-example"  # Default project name

    # Initialize a run to log some sample data
    with wandb.init(project=project, name="sample_run") as run:
        for step in range(100):
            wandb.log({
                "Step": step,
                # "val_loss": 1.0 / (step + 1),
                # "val_accuracy": step / 100.0,
                # "train_loss": 1.0 / (step + 2),
                # "train_accuracy": step / 110.0,
                "f1_score": step / 100.0,
                "recall": step / 120.0,
                
            })
    return project

# Create a new project and log data
project = create_project_and_log_data()
entity = wandb.Api().default_entity