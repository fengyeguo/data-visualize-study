import numpy as np
from sklearn.metrics import confusion_matrix

# Example data
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 0, 1, 0, 0]

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Extract values from confusion matrix
TN, FP, FN, TP = cm.ravel()
print(f"TN: {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

# Calculate Precision and Recall
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# 在上述代码中，confusion_matrix 函数的输入是 y_true 和 y_pred，其中 y_pred 是模型的预测结果。
# 这里没有涉及显式的阈值概念，因为 y_pred 已经是二值化的预测结果（即 0 或 1）。
# 通常情况下，模型（比如二分类的逻辑回归模型或神经网络）输出的预测值是一个概率，表示某个样本属于正类的概率。
# 这时，你可以通过设定一个阈值（默认一般为 0.5）将概率值转化为二进制类别。如果你想调整阈值（比如改为 0.6 或其他值），可以基于概率预测值手动二值化 y_pred，再计算混淆矩阵。

# Example data
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred_prob = [0.9, 0.6, 0.8, 0.3, 0.2, 0.7, 0.1, 0.6, 0.4, 0.2]

# Set threshold
threshold = 0.5

# Convert probabilities to binary predictions based on the threshold
y_pred = [1 if prob >= threshold else 0 for prob in y_pred_prob]

# Compute confusion matrix
cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:")
print(cm)

# Extract values from confusion matrix
TN, FP, FN, TP = cm.ravel()
print(f"TN: {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

# Calculate Precision and Recall
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# 改变阈值的影响：
# 提高阈值意味着模型会更加谨慎地预测正类，只有高于该阈值的样本才会被预测为正类，这通常会提高精度（precision），但可能会降低召回率（recall）。
# 降低阈值则会增加正类的预测数量，通常会提高召回率，但可能降低精度。
