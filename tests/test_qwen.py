import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.qwen_client import generate_code


prompt = """
Write a C++ program that takes two integers as input,
adds them, and displays the result.

Return only the C++ source code.
"""

result = generate_code(prompt)

print("\n===== QWEN GENERATED CODE =====\n")
print(result)