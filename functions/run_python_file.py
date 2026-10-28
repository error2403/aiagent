import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    
        # Check if target file is within the working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # check that target file is a file
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # check that it is a python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # start building command to run
        command = ["python", abs_file_path]
        if args is not None:
            command.extend(args)

        completed_process = subprocess.run(command,
                                       cwd=working_directory,
                                       capture_output=True,
                                       text=True,
                                       timeout=30)

        # build output string
        output = ""
        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode} "
        if completed_process.stdout == '' and completed_process.stderr == '':
            output += "No output produced "
        if not completed_process.stdout == '':
            output += f"STDOUT: {completed_process.stdout} "
        if not completed_process.stderr == '':
            output += f"STDERR: {completed_process.stderr} "
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"