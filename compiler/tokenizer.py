import re


# Keywords supported by our controlled natural language
KEYWORDS = {
    "declare": "DECLARE",
    "integer": "INTEGER",
    "float": "FLOAT",
    "read": "READ",
    "input": "INPUT",
    "display": "DISPLAY",
    "print": "DISPLAY",
    "show": "DISPLAY",
    "set": "SET",
    "to": "TO",
    "add": "ADD",
    
    "subtract": "SUBTRACT",
    "minus": "SUBTRACT",
    "multiply": "MULTIPLY",
    "product": "MULTIPLY",
    "divide": "DIVIDE",
    "by": "BY",
    "store": "STORE",
    "in": "IN",
    "and": "AND",
    "if": "IF",
    "else": "ELSE",
    "otherwise": "OTHERWISE",
    "then": "THEN",
    "repeat": "REPEAT",
    "times": "TIMES",
    "while": "WHILE",
    "greater": "GREATER",
    "less": "LESS",
    "equal": "EQUAL",
}


def tokenize_sentence(sentence):
    """
    Convert one controlled-English sentence
    into a list of (lexeme, token_type).
    """

    sentence = sentence.strip().lower()

    # Remove punctuation that is not important
    sentence = re.sub(r"[.,!?]", "", sentence)

    words = sentence.split()

    tokens = []

    for word in words:

        # Number
        if word.isdigit():
            tokens.append((word, "NUMBER"))

        # Keyword
        elif word in KEYWORDS:
            tokens.append((word, KEYWORDS[word]))

        # Identifier
        elif re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", word):
            tokens.append((word, "IDENTIFIER"))

        else:
            tokens.append((word, "UNKNOWN"))

    return tokens


def tokenize_program(program):
    """
    Tokenize every sentence/line in a natural-language program.
    """

    lines = program.splitlines()

    result = []

    for line_number, line in enumerate(lines, start=1):

        if not line.strip():
            continue

        tokens = tokenize_sentence(line)

        result.append({
            "line": line_number,
            "tokens": tokens
        })

    return result