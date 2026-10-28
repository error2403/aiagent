import os

from config import MAX_READ_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
	try:
		abs_working_dir = os.path.abspath(working_directory)
		abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

		# Check if target file is within the working directory
		if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
			return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

		# check that file_path points to a file
		if not os.path.isfile(abs_file_path):
			return f'Error: File not found or is not a regular file: "{file_path}"'

    	# read contents of file
		with open(abs_file_path, 'r') as f:
			content = f.read(MAX_READ_CHARS)

        	# check if there is more to read & file is truncated
			if f.read(1):
				content += f'[...File "{file_path}" truncated at {MAX_READ_CHARS} characters]'

			return content

	except Exception as e:
		return f'Error: reading file "{file_path}": {e}'

