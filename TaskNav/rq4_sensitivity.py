import matplotlib.pyplot as plt


def plot_sensitivity():
    # 模拟论文 Figure (a) Few-shot 数量对 F1 的影响
    few_shot_k = [1, 2, 4, 6, 8, 10, 15]
    f1_scores_k = [0.72, 0.76, 0.81, 0.85, 0.84, 0.83, 0.82]

    # 模拟论文 Figure (b) SC runs 数量对 F1 的影响
    sc_runs = [1, 3, 5, 7, 10]
    f1_scores_sc = [0.78, 0.81, 0.85, 0.855, 0.852]

    print("--- RQ4: Parameter Sensitivity Analysis ---")
    print(f"Optimal Few-shot examples: 6 (F1={max(f1_scores_k)})")
    print(f"Optimal SC runs: 5 (F1={f1_scores_sc[2]})")

    # 取消注释以生成绘图
    # plt.figure(figsize=(10, 4))
    # plt.subplot(1, 2, 1)
    # plt.plot(few_shot_k, f1_scores_k, marker='o')
    # plt.title('Impact of Few-shot Exemplars')
    # plt.xlabel('Number of Examples')
    # plt.ylabel('F1 Score')
    # plt.subplot(1, 2, 2)
    # plt.plot(sc_runs, f1_scores_sc, marker='o', color='orange')
    # plt.title('Impact of Self-Consistency Runs')
    # plt.xlabel('Number of Runs')
    # plt.show()


plot_sensitivity()