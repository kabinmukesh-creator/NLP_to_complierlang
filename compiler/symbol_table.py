class SymbolTableError(Exception):
    pass


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def declare(self, name, datatype, line=None):
        """
        Add a variable to the symbol table.
        """

        if name in self.symbols:
            raise SymbolTableError(
                f"Variable '{name}' is already declared."
            )

        self.symbols[name] = {
            "type": datatype,
            "line": line
        }

    def exists(self, name):
        """
        Check whether a variable exists.
        """

        return name in self.symbols

    def get(self, name):
        """
        Get information about a variable.
        """

        if name not in self.symbols:
            raise SymbolTableError(
                f"Variable '{name}' has not been declared."
            )

        return self.symbols[name]

    def get_type(self, name):
        """
        Get the datatype of a variable.
        """

        return self.get(name)["type"]

    def display(self):
        """
        Return the symbol table.
        """

        return self.symbols