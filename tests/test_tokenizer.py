import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program


program = """
Declare integer a.
Declare integer b.
Read a.
Read b.
Add a and b and store in total.
Display total.
"""


result = tokenize_program(program)


print("\n===== TOKENIZATION RESULT =====\n")

for line in result:
    print(f"Line {line['line']}:")

    for lexeme, token_type in line["tokens"]:
        print(f"    {lexeme:<12} -> {token_type}")

    print()