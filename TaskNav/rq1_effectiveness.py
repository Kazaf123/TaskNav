import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score, mean_absolute_error
from scipy.stats import spearmanr


def evaluate_rq1(y_true_binary, y_pred_binary, y_true_scores, y_pred_scores):
    # 分类指标: Precision, Recall, F1
    precision = precision_score(y_true_binary, y_pred_binary)
    recall = recall_score(y_true_binary, y_pred_binary)
    f1 = f1_score(y_true_binary, y_pred_binary)

    # 回归/排序指标: MAE, Spearman Correlation
    mae = mean_absolute_error(y_true_scores, y_pred_scores)
    spearman_rho, _ = spearmanr(y_true_scores, y_pred_scores)

    print("--- RQ1: Effectiveness Results ---")
    print(f"Precision: {precision:.2f}")
    print(f"Recall:    {recall:.2f}")
    print(f"F1-Score:  {f1:.2f}")
    print(f"MAE:       {mae:.2f}")
    print(f"Spearman:  {spearman_rho:.2f}")


# 模拟数据验证
y_true_bin = [1, 0, 1, 1, 0]  # 1 为冗余
y_pred_bin = [1, 0, 1, 0, 0]
y_true_score = [0, 2, 0, 1, 2]  # 0无关(冗余), 1辅助, 2核心
y_pred_score = [0, 2, 0, 2, 1]

evaluate_rq1(y_true_bin, y_pred_bin, y_true_score, y_pred_score)