from ui_extractor import UIExtractor
from llm_reasoner import LLMReasoner
from ui_pruner import UIPruner


def main():
    api_key = "YOUR_GEMINI_API_KEY"
    task = "Start navigation to a destination"
    xml_path = "sample_ui.xml"
    screenshot_path = "sample_screenshot.png"

    print("=== TaskNav Pipeline Started ===")

    # 1. 提取多模态 UI 表示
    extractor = UIExtractor()
    components = extractor.extract_multimodal_representation(xml_path, screenshot_path)
    print(f"Extracted {len(components)} UI components.")

    # 2. 任务感知关联性推理
    reasoner = LLMReasoner(api_key=api_key)
    print("Querying LLM for relevance scoring (with Self-Consistency)...")
    relevance_scores = reasoner.infer_relevance(task, components, k=5)

    # 3. 非侵入式界面修剪策略生成
    pruner = UIPruner(threshold=1)
    pruning_strategy = pruner.generate_pruning_strategy(components, relevance_scores)
    pruner.export_policy_for_android(pruning_strategy)

    print("=== Pipeline Completed ===")


if __name__ == "__main__":
    main()