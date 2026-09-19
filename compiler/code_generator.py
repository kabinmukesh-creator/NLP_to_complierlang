class CodeGenerator:

    def __init__(self):
        self.code = []

    def generate_instruction(self, instruction):

        operation = instruction.operation
        operands = instruction.operands

        # -------------------------
        # Declaration
        # -------------------------

        if operation == "DECL":

            datatype = operands[0]
            variable = operands[1]

            self.code.append(
                f"{datatype} {variable};"
            )

        # -------------------------
        # Input
        # -------------------------

        elif operation == "INPUT":

            variable = operands[0]

            self.code.append(
                f"cin >> {variable};"
            )

        # -------------------------
        # Output
        # -------------------------

        elif operation == "OUTPUT":

            variable = operands[0]

            self.code.append(
                f"cout << {variable} << endl;"
            )

        # -------------------------
        # Assignment
        # -------------------------

        elif operation == "ASSIGN":

            variable = operands[0]
            value = operands[1]

            self.code.append(
                f"{variable} = {value};"
            )

        # -------------------------
        # Addition
        # -------------------------

        elif operation == "ADD":

            left = operands[0]
            right = operands[1]
            destination = operands[2]

            self.code.append(
                f"{destination} = {left} + {right};"
            )

    def generate(self, instructions):

        self.code = []

        # Header
        self.code.append("#include <iostream>")
        self.code.append("")
        self.code.append("using namespace std;")
        self.code.append("")
        self.code.append("int main() {")
        self.code.append("")

        # Generate statements
        for instruction in instructions:

            self.generate_instruction(instruction)

            # Indent generated C++
            if self.code:
                self.code[-1] = "    " + self.code[-1]

        # Footer
        self.code.append("")
        self.code.append("    return 0;")
        self.code.append("}")

        return "\n".join(self.code)