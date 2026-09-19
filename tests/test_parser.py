import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.tokenizer import tokenize_program
from compiler.parser import parse_program


program = """
Declare integer a.
Declare integer b.
Read a.
Read b.
Add a and b and store in total.
Display total.
"""


tokens = tokenize_program(program)

statements = parse_program(tokens)


print("\n===== PARSER RESULT =====\n")

for statement in statements:
    print(statement)