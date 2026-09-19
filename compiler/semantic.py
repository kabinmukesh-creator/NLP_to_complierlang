from compiler.symbol_table import SymbolTable


class SemanticError(Exception):
    pass


class SemanticAnalyzer:

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []

    def analyze_declaration(self, statement):
        variable = statement["variable"]
        datatype = statement["datatype"]
        line = statement["line"]

        try:
            self.symbol_table.declare(
                variable,
                datatype,
                line
            )

        except Exception as error:
            self.errors.append({
                "line": line,
                "message": str(error)
            })

    def analyze_input(self, statement):
        variable = statement["variable"]
        line = statement["line"]

        if not self.symbol_table.exists(variable):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{variable}' "
                    f"has not been declared."
            })

    def analyze_output(self, statement):
        variable = statement["value"]
        line = statement["line"]

        if not self.symbol_table.exists(variable):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{variable}' "
                    f"has not been declared."
            })

    def analyze_assignment(self, statement):
        variable = statement["variable"]
        value = statement["value"]
        line = statement["line"]

        # Check destination variable
        if not self.symbol_table.exists(variable):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{variable}' "
                    f"has not been declared."
            })

        # If value is an identifier,
        # make sure that identifier exists.
        if not value.isdigit():

            if not self.symbol_table.exists(value):
                self.errors.append({
                    "line": line,
                    "message":
                        f"Variable '{value}' "
                        f"has not been declared."
                })

    def analyze_addition(self, statement):
        left = statement["left"]
        right = statement["right"]
        destination = statement["destination"]
        line = statement["line"]

        # Check left operand
        if not self.symbol_table.exists(left):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{left}' "
                    f"has not been declared."
            })

        # Check right operand
        if not self.symbol_table.exists(right):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{right}' "
                    f"has not been declared."
            })

        # Check destination
        if not self.symbol_table.exists(destination):
            self.errors.append({
                "line": line,
                "message":
                    f"Variable '{destination}' "
                    f"has not been declared."
            })

    def analyze_statement(self, statement):

        statement_type = statement["type"]

        if statement_type == "DECLARATION":
            self.analyze_declaration(statement)

        elif statement_type == "INPUT":
            self.analyze_input(statement)

        elif statement_type == "OUTPUT":
            self.analyze_output(statement)

        elif statement_type == "ASSIGNMENT":
            self.analyze_assignment(statement)

        elif statement_type == "ADDITION":
            self.analyze_addition(statement)

        elif statement_type == "ERROR":
            self.errors.append({
                "line": statement["line"],
                "message": statement["message"]
            })

    def analyze(self, statements):

        for statement in statements:
            self.analyze_statement(statement)

        return {
            "success": len(self.errors) == 0,
            "errors": self.errors,
            "symbol_table": self.symbol_table.display()
        }