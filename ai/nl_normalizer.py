from ai.qwen_client import generate_code


SYSTEM_INSTRUCTIONS = """
You are the natural-language front end of a compiler.

Your job is to convert the user's English programming requirement
into our controlled compiler language.

Do NOT generate C++.
Do NOT generate Python.
Do NOT explain anything.
Return ONLY the controlled compiler statements.

Supported statements:

Declare integer <name>.
Declare float <name>.

Read <name>.

Display <name>.

Set <name> to <number>.
Set <name> to <name>.

Add <name> and <name> and store in <name>.

Subtract <name> and <name> and store in <name>.

Multiply <name> and <name> and store in <name>.

Divide <name> by <name> and store in <name>.

Rules:

1. Every variable must be declared before it is used.
2. Use simple variable names.
3. Use one statement per line.
4. End every statement with a period.
5. Do not add comments.
6. Do not add Markdown.
7. Do not add explanations.
8. If the user asks for output, use Display.
9. If the user asks for input, use Read.
10. For arithmetic, use the supported arithmetic statement format.
"""


def normalize_request(user_request: str) -> str:

    prompt = f"""
{SYSTEM_INSTRUCTIONS}

User requirement:
{user_request}

Return only the controlled compiler program.
"""

    return generate_code(prompt).strip()