import time


def evaluate_efficiency(llm_func, app_components):
    start_time = time.time()

    # 模拟 LLM 推理调用
    input_tokens = len(str(app_components)) // 4  # 简单估算
    # llm_func(app_components)
    output_tokens = 150  # 假设输出 token

    execution_time = time.time() - start_time
    total_tokens = input_tokens + output_tokens

    # 按照 API 定价计算 (假设 input: $0.5/1M, output: $1.5/1M)
    cost = (input_tokens * 0.5 + output_tokens * 1.5) / 1000000

    print("--- RQ2: Efficiency Results ---")
    print(f"Time (s/app):  {execution_time:.2f}")
    print(f"Tokens (app):  {total_tokens}")
    print(f"Cost ($/app):  {cost:.4f}")


evaluate_efficiency(None, "Sample components string " * 500)