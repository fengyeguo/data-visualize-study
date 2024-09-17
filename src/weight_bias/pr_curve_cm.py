import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc
import matplotlib.pyplot as plt

# Example data
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred_prob = [0.9, 0.4, 0.8, 0.3, 0.2, 0.7, 0.1, 0.6, 0.4, 0.2]

# Compute precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_true, y_pred_prob)

# Calculate AUC for Precision-Recall curve
pr_auc = auc(recall, precision)

# Plot the precision-recall curve
plt.figure()
plt.plot(recall, precision, label=f'PR curve (area = {pr_auc:.2f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='best')
plt.grid(True)
# plt.savefig('precision_recall_curve.png')  # 保存为PNG文件

plt.show()