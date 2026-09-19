import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program
from compiler.semantic import SemanticAnalyzer
from compiler.ir import IRGenerator
from compiler.code_generator import CodeGenerator


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

if not semantic_result["success"]:

    print("Semantic errors found:")

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
# C++ Generation
# --------------------------------

generator = CodeGenerator()

cpp_code = generator.generate(instructions)


# --------------------------------
# Display
# --------------------------------

print("\n===== GENERATED C++ CODE =====\n")

print(cpp_code)