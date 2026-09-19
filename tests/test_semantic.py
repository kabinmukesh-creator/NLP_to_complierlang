import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program
from compiler.semantic import SemanticAnalyzer


# --------------------------------
# Test program
# --------------------------------

program = """
Declare integer a.
Declare integer b.
Declare integer total.
Read a.
Read b.
Add a and b and store in total.
Display total.
"""


# --------------------------------
# Tokenization
# --------------------------------

tokens = tokenize_program(program)


# --------------------------------
# Parsing
# --------------------------------

statements = parse_program(tokens)


# --------------------------------
# Semantic Analysis
# --------------------------------

analyzer = SemanticAnalyzer()

result = analyzer.analyze(statements)


# --------------------------------
# Display results
# --------------------------------

print("\n===== SEMANTIC ANALYSIS =====\n")

print("Success:", result["success"])

print("\nErrors:")

if result["errors"]:
    for error in result["errors"]:
        print(
            f"Line {error['line']}: "
            f"{error['message']}"
        )
else:
    print("No semantic errors.")


print("\nSymbol Table:")

for name, information in result["symbol_table"].items():
    print(
        f"{name:<10} "
        f"{information['type']:<10} "
        f"line={information['line']}"
    )