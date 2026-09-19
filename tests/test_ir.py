import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program
from compiler.semantic import SemanticAnalyzer
from compiler.ir import IRGenerator


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

semantic_result = analyzer.analyze(statements)


print("\n===== SEMANTIC RESULT =====\n")

print("Success:", semantic_result["success"])


if not semantic_result["success"]:

    print("\nSemantic Errors:")

    for error in semantic_result["errors"]:
        print(
            f"Line {error['line']}: "
            f"{error['message']}"
        )

    sys.exit(1)


# --------------------------------
# IR Generation
# --------------------------------

ir_generator = IRGenerator()

instructions = ir_generator.generate(statements)


# --------------------------------
# Display IR
# --------------------------------

print("\n===== INTERMEDIATE REPRESENTATION =====\n")

for index, instruction in enumerate(instructions, start=1):

    print(
        f"{index:02d}. {instruction}"
    )