import sys
from pathlib import Path

# Add project root to Python import path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from compiler.gcc_runner import compile_and_run


code = """
#include <iostream>
using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    cout << a + b << endl;

    return 0;
}
"""


result = compile_and_run(
    code,
    "10 20\n"
)


print("\n===== GCC RESULT =====\n")

print("Compiled:", result["compiled"])
print("Compile Error:", result["compile_error"])
print("Execution Success:", result["execution_success"])
print("Output:", result["output"])
print("Execution Error:", result["execution_error"])