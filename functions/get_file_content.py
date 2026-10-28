import os

def get_file_content(working_directory: str, file_path: str) -> str:
	abs_working_dir = os.path.abspath(working_directory)
	target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

	# Check if target file is within the working directory
	valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

	if not valid_target_file:
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

	# check that target dir is a dir
	if not os.path.isfile(target_file):
		return f'Error: File not found or is not a regular file: "{file_path}"'

    # read contents of file
	with open(target_file, 'r') as f:
		content = f.read(10_000)

        # After reading the first MAX_READ_CHARS
		if f.read(1):
			content += f'[...File "{file_path}" truncated at {10_000} characters]'

		return content