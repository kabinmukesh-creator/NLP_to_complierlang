import subprocess
import tempfile
from pathlib import Path


def clean_code(code: str) -> str:
    """
    Remove Markdown code fences if the LLM returns them.
    """
    code = code.strip()

    if code.startswith("```"):
        lines = code.splitlines()

        # Remove first line: ```cpp / ```
        lines = lines[1:]

        # Remove final ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        code = "\n".join(lines)

    return code.strip()


def compile_and_run(code: str, user_input: str = "") -> dict:
    """
    Compile and execute generated C++ code using g++.

    This is a local development version.
    Sandboxing will be added later.
    """

    code = clean_code(code)

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_path = Path(temp_dir)

        source_file = temp_path / "program.cpp"
        executable_file = temp_path / "program.exe"

        # Write generated C++ code
        source_file.write_text(
            code,
            encoding="utf-8"
        )

        # -------------------------
        # Compilation
        # -------------------------

        compile_result = subprocess.run(
            [
                "g++",
                str(source_file),
                "-std=c++17",
                "-o",
                str(executable_file)
            ],
            capture_output=True,
            text=True,
            timeout=30
        )

        if compile_result.returncode != 0:
            return {
                "compiled": False,
                "compile_error": compile_result.stderr,
                "execution_success": False,
                "output": "",
                "execution_error": ""
            }

        # -------------------------
        # Execution
        # -------------------------

        try:
            execution_result = subprocess.run(
                [str(executable_file)],
                input=user_input,
                capture_output=True,
                text=True,
                timeout=5
            )

            return {
                "compiled": True,
                "compile_error": "",
                "execution_success": execution_result.returncode == 0,
                "output": execution_result.stdout,
                "execution_error": execution_result.stderr
            }

        except subprocess.TimeoutExpired:
            return {
                "compiled": True,
                "compile_error": "",
                "execution_success": False,
                "output": "",
                "execution_error": "Program execution timed out."
            }