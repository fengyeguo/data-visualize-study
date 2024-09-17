import wandb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve

# Initialize a new wandb run
wandb.init(project='pr_proj', name='pr_curve_example')

# Example data - replace with your own data
y_true = np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8, 0.7, 0.2, 0.9, 0.3, 0.6, 0.5])

# Compute precision-recall curve
precision, recall, _ = precision_recall_curve(y_true, y_scores)

# Plot PR curve
plt.figure()
plt.plot(recall, precision, marker='.')
plt.title('Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.grid(True)

# Save the plot to a file
plt.savefig('pr_curve.png')
plt.close()

# Log the plot to wandb
wandb.log({"PR Curve": wandb.Image('pr_curve.png')})

# Finish the wandb run
wandb.finish()
