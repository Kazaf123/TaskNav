import google.generativeai as genai
from collections import Counter
import json
import re


class LLMReasoner:
    def __init__(self, api_key, model_name="gemini-3-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.system_instruction = "You are an expert in mobile GUI accessibility analysis."

    def construct_prompt(self, task_description, components):
        """构建包含 Few-shot 的任务感知 Prompt"""
        prompt = f"""
        Role: {self.system_instruction}

        Task:
        The user wants to: {task_description}

        Scoring Criteria:
        - 2 = Core functionality (essential for completing the task)
        - 1 = Auxiliary functionality (helpful but not necessary)
        - 0 = Irrelevant (unrelated to the task)

        Example Task: Start navigation to a destination
        Component A: Text: 'Search', Type: Input Field -> Score: 2
        Component B: Text: 'Nearby Restaurants', Type: List -> Score: 1
        Component C: Text: 'Advertisement', Type: Image Banner -> Score: 0

        Current UI Components:
        """
        for comp in components:
            prompt += f"Component ID: {comp['id']}\nText: '{comp['text']}'\nType: {comp['type']}\nHierarchy: {comp['hierarchy']}\n\n"

        prompt += """
        For each component, determine its relevance to the task. Think step-by-step.
        Output exactly in this format:
        Component ID: [ID], Score: [Score], Reason: [Reason]
        """
        return prompt

    def parse_response(self, text):
        """解析 LLM 输出"""
        scores = {}
        pattern = r"Component ID:\s*(\d+),\s*Score:\s*(\d)"
        matches = re.findall(pattern, text)
        for match in matches:
            scores[int(match[0])] = int(match[1])
        return scores

    def infer_relevance(self, task_description, components, k=5):
        """实现 Self-Consistency 多数投票机制"""
        prompt = self.construct_prompt(task_description, components)
        all_run_scores = []

        # 运行 k 次
        for _ in range(k):
            response = self.model.generate_content(prompt)
            scores = self.parse_response(response.text)
            all_run_scores.append(scores)

        # 多数投票聚合
        final_scores = {}
        for comp in components:
            cid = comp['id']
            votes = [run.get(cid, 0) for run in all_run_scores if cid in run]
            if votes:
                majority_score = Counter(votes).most_common(1)[0][0]
                final_scores[cid] = majority_score
            else:
                final_scores[cid] = 0  # 默认无关

        return final_scores