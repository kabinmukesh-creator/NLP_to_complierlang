class IRInstruction:
    def __init__(self, operation, *operands):
        self.operation = operation
        self.operands = operands

    def __repr__(self):
        if self.operands:
            return f"{self.operation} " + " ".join(
                str(operand) for operand in self.operands
            )

        return self.operation


class IRGenerator:

    def __init__(self):
        self.instructions = []

    def generate_statement(self, statement):

        statement_type = statement["type"]

        # -------------------------
        # Declaration
        # -------------------------

        if statement_type == "DECLARATION":

            self.instructions.append(
                IRInstruction(
                    "DECL",
                    statement["datatype"],
                    statement["variable"]
                )
            )

        # -------------------------
        # Input
        # -------------------------

        elif statement_type == "INPUT":

            self.instructions.append(
                IRInstruction(
                    "INPUT",
                    statement["variable"]
                )
            )

        # -------------------------
        # Output
        # -------------------------

        elif statement_type == "OUTPUT":

            self.instructions.append(
                IRInstruction(
                    "OUTPUT",
                    statement["value"]
                )
            )

        # -------------------------
        # Assignment
        # -------------------------

        elif statement_type == "ASSIGNMENT":

            self.instructions.append(
                IRInstruction(
                    "ASSIGN",
                    statement["variable"],
                    statement["value"]
                )
            )

        # -------------------------
        # Addition
        # -------------------------

        elif statement_type == "ADDITION":

            self.instructions.append(
                IRInstruction(
                    "ADD",
                    statement["left"],
                    statement["right"],
                    statement["destination"]
                )
            )

        # -------------------------
        # Ignore errors
        # -------------------------

        elif statement_type == "ERROR":

            return

    def generate(self, statements):

        self.instructions = []

        for statement in statements:
            self.generate_statement(statement)

        return self.instructions