import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.nl_normalizer import normalize_request


user_request = """
I need a program where the user enters two numbers.
Calculate their sum and show the answer.
"""


print("\n===== USER REQUEST =====\n")

print(user_request)


print("\n===== QWEN NORMALIZATION =====\n")

result = normalize_request(user_request)

print(result)