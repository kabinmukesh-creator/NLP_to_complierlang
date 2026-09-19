import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program
from compiler.semantic import SemanticAnalyzer
from compiler.ir import IRGenerator
from compiler.code_generator import CodeGenerator
from compiler.gcc_runner import compile_and_run


# ==========================================
# 1. Controlled Natural Language Program
# ==========================================

program = """
Declare integer a.
Declare integer b.
Declare integer total.
Read a.
Read b.
Add a and b and store in total.
Display total.
"""


# ==========================================
# 2. TOKENIZATION
# ==========================================

print("\n===== 1. TOKENIZATION =====\n")

tokens = tokenize_program(program)

for line in tokens:
    print(f"Line {line['line']}:")

    for lexeme, token_type in line["tokens"]:
        print(f"    {lexeme:<12} -> {token_type}")


# ==========================================
# 3. PARSING
# ==========================================

print("\n===== 2. PARSING =====\n")

statements = parse_program(tokens)

for statement in statements:
    print(statement)


# ==========================================
# 4. SEMANTIC ANALYSIS
# ==========================================

print("\n===== 3. SEMANTIC ANALYSIS =====\n")

analyzer = SemanticAnalyzer()

semantic_result = analyzer.analyze(statements)

print("Success:", semantic_result["success"])

if not semantic_result["success"]:

    print("\nSemantic Errors:")

    for error in semantic_result["errors"]:
        print(
            f"Line {error['line']}: "
            f"{error['message']}"
        )

    sys.exit(1)

print("No semantic errors.")

print("\nSymbol Table:")

for name, information in semantic_result["symbol_table"].items():

    print(
        f"{name:<10} "
        f"{information['type']:<10} "
        f"line={information['line']}"
    )


# ==========================================
# 5. INTERMEDIATE REPRESENTATION
# ==========================================

print("\n===== 4. INTERMEDIATE REPRESENTATION =====\n")

ir_generator = IRGenerator()

instructions = ir_generator.generate(statements)

for index, instruction in enumerate(
    instructions,
    start=1
):
    print(
        f"{index:02d}. {instruction}"
    )


# ==========================================
# 6. C++ CODE GENERATION
# ==========================================

print("\n===== 5. GENERATED C++ =====\n")

generator = CodeGenerator()

cpp_code = generator.generate(instructions)

print(cpp_code)


# ==========================================
# 7. GCC COMPILATION + EXECUTION
# ==========================================

print("\n===== 6. GCC EXECUTION =====\n")

result = compile_and_run(
    cpp_code,
    "10 20\n"
)


print("Compiled:", result["compiled"])

if not result["compiled"]:

    print("\nCompilation Error:")
    print(result["compile_error"])

    sys.exit(1)


print(
    "Execution Success:",
    result["execution_success"]
)

print(
    "Program Output:",
    result["output"]
)

if result["execution_error"]:

    print(
        "Execution Error:",
        result["execution_error"]
    )