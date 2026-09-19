class ParserError(Exception):
    pass


def parse_declaration(tokens):
    # DECLARE INTEGER IDENTIFIER
    if len(tokens) == 3:
        if (
            tokens[0][1] == "DECLARE"
            and tokens[1][1] in ("INTEGER", "FLOAT")
            and tokens[2][1] == "IDENTIFIER"
        ):
            datatype = "int" if tokens[1][1] == "INTEGER" else "float"

            return {
                "type": "DECLARATION",
                "datatype": datatype,
                "variable": tokens[2][0]
            }

    return None


def parse_input(tokens):
    # READ IDENTIFIER
    if len(tokens) == 2:
        if (
            tokens[0][1] in ("READ", "INPUT")
            and tokens[1][1] == "IDENTIFIER"
        ):
            return {
                "type": "INPUT",
                "variable": tokens[1][0]
            }

    return None


def parse_output(tokens):
    # DISPLAY IDENTIFIER
    if len(tokens) == 2:
        if (
            tokens[0][1] == "DISPLAY"
            and tokens[1][1] == "IDENTIFIER"
        ):
            return {
                "type": "OUTPUT",
                "value": tokens[1][0]
            }

    return None


def parse_assignment(tokens):
    # SET IDENTIFIER TO NUMBER
    if len(tokens) == 4:
        if (
            tokens[0][1] == "SET"
            and tokens[1][1] == "IDENTIFIER"
            and tokens[2][1] == "TO"
            and tokens[3][1] in ("NUMBER", "IDENTIFIER")
        ):
            return {
                "type": "ASSIGNMENT",
                "variable": tokens[1][0],
                "value": tokens[3][0]
            }

    return None


def parse_addition(tokens):
    """
    Example:

    Add a and b and store in total.
    """

    if not tokens:
        return None

    if tokens[0][1] != "ADD":
        return None

    identifiers = [
        token[0]
        for token in tokens
        if token[1] == "IDENTIFIER"
    ]

    if len(identifiers) != 3:
        raise ParserError(
            "Invalid addition statement. "
            "Expected: Add <a> and <b> and store in <result>."
        )

    return {
        "type": "ADDITION",
        "left": identifiers[0],
        "right": identifiers[1],
        "destination": identifiers[2]
    }


def parse_statement(tokens):

    parsers = [
        parse_declaration,
        parse_input,
        parse_output,
        parse_assignment,
        parse_addition
    ]

    for parser in parsers:
        result = parser(tokens)

        if result is not None:
            return result

    raise ParserError("Unsupported or invalid statement.")


def parse_program(tokenized_program):

    parsed_statements = []

    for line in tokenized_program:

        line_number = line["line"]
        tokens = line["tokens"]

        try:
            statement = parse_statement(tokens)
            statement["line"] = line_number

            parsed_statements.append(statement)

        except ParserError as error:

            parsed_statements.append({
                "type": "ERROR",
                "line": line_number,
                "message": str(error)
            })

    return parsed_statements