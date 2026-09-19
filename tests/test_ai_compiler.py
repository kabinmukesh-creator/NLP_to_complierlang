import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from ai.nl_normalizer import normalize_request
from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program
from compiler.semantic import SemanticAnalyzer
from compiler.ir import IRGenerator
from compiler.code_generator import CodeGenerator
from compiler.gcc_runner import compile_and_run


# ==========================================
# 1. USER'S NATURAL LANGUAGE
# ==========================================

user_request = """
I need a program where the user enters two numbers.
Calculate their sum and show the answer.
"""


print("\n========================================")
print("USER REQUEST")
print("========================================\n")

print(user_request)


# ==========================================
# 2. QWEN NORMALIZATION
# ==========================================

print("\n========================================")
print("QWEN → CONTROLLED LANGUAGE")
print("========================================\n")

controlled_program = normalize_request(user_request)

print(controlled_program)


# ==========================================
# 3. TOKENIZATION
# ==========================================

print("\n========================================")
print("TOKENIZATION")
print("========================================\n")

tokens = tokenize_program(controlled_program)

for line in tokens:

    print(f"Line {line['line']}:")

    for lexeme, token_type in line["tokens"]:
        print(
            f"    {lexeme:<12} -> {token_type}"
        )


# ==========================================
# 4. PARSING
# ==========================================

print("\n========================================")
print("PARSING")
print("========================================\n")

statements = parse_program(tokens)

for statement in statements:
    print(statement)


# ==========================================
# 5. SEMANTIC ANALYSIS
# ==========================================

print("\n========================================")
print("SEMANTIC ANALYSIS")
print("========================================\n")

analyzer = SemanticAnalyzer()

semantic_result = analyzer.analyze(statements)

print(
    "Semantic Success:",
    semantic_result["success"]
)

if not semantic_result["success"]:

    print("\nSemantic Errors:")

    for error in semantic_result["errors"]:

        print(
            f"Line {error['line']}: "
            f"{error['message']}"
        )

    sys.exit(1)


print("No semantic errors.")


# ==========================================
# 6. SYMBOL TABLE
# ==========================================

print("\n========================================")
print("SYMBOL TABLE")
print("========================================\n")

for name, information in semantic_result[
    "symbol_table"
].items():

    print(
        f"{name:<12}"
        f"{information['type']:<10}"
        f"line={information['line']}"
    )


# ==========================================
# 7. IR GENERATION
# ==========================================

print("\n========================================")
print("INTERMEDIATE REPRESENTATION")
print("========================================\n")

ir_generator = IRGenerator()

instructions = ir_generator.generate(
    statements
)

for index, instruction in enumerate(
    instructions,
    start=1
):

    print(
        f"{index:02d}. {instruction}"
    )


# ==========================================
# 8. C++ GENERATION
# ==========================================

print("\n========================================")
print("GENERATED C++")
print("========================================\n")

code_generator = CodeGenerator()

cpp_code = code_generator.generate(
    instructions
)

print(cpp_code)


# ==========================================
# 9. GCC COMPILATION + EXECUTION
# ==========================================

print("\n========================================")
print("GCC COMPILATION + EXECUTION")
print("========================================\n")

result = compile_and_run(
    cpp_code,
    "10 20\n"
)


print(
    "Compiled:",
    result["compiled"]
)

print(
    "Execution Success:",
    result["execution_success"]
)

print(
    "Program Output:",
    result["output"]
)


if result["compile_error"]:

    print("\nCompilation Error:")
    print(result["compile_error"])


if result["execution_error"]:

    print("\nExecution Error:")
    print(result["execution_error"])