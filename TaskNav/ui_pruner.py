class UIPruner:
    def __init__(self, threshold=1):
        self.threshold = threshold

    def generate_pruning_strategy(self, components, relevance_scores):
        """
        生成非侵入式修剪指令。
        得分 < 1 (即得分为 0 的无关组件) 将被屏蔽和视觉遮蔽。
        """
        pruning_actions = []
        for comp in components:
            score = relevance_scores.get(comp['id'], 0)
            if score < self.threshold:
                action = {
                    "component_id": comp['id'],
                    "bounds": comp['bounds'],
                    "action_suppress": True,
                    "visual_mask": True,
                    "reason": "Irrelevant to current task"
                }
                pruning_actions.append(action)
            else:
                action = {
                    "component_id": comp['id'],
                    "action_suppress": False,
                    "visual_mask": False,
                    "reason": "Core or Auxiliary functionality"
                }
                pruning_actions.append(action)

        return pruning_actions

    def export_policy_for_android(self, pruning_actions, output_path="pruning_policy.json"):
        """导出 JSON 供 Android 端的 AccessibilityService 读取执行"""
        with open(output_path, 'w') as f:
            json.dump(pruning_actions, f, indent=4)
        print(f"Pruning policy exported to {output_path}")