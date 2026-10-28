import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
	abs_working_dir = os.path.abspath(working_directory)
	target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

	# Check if target file is within the working directory
	valid_target_file = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

	if not valid_target_file:
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

	# check that target dir is a dir
	if os.path.isdir(target_file):
		return f'Error: Cannot write to "{file_path}" as it is a directory'

	# make sure all parent directories exist
	os.makedirs(os.path.dirname(target_file), exist_ok=True)

	# open and write to file
	with open(target_file, 'w') as f:
		f.write(content)

	return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'