import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
	abs_working_dir = os.path.abspath(working_directory)
	target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

	# Check if target dir is within the working directory
	valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

	if not valid_target_dir:
		return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

	# check that target dir is a dir
	if not os.path.isdir(target_dir):
		return f'Error: "{directory}" is not a directory'

	# collect all items in provided directory
	content_str = ""
	for item in os.listdir(target_dir):
		item_path = os.path.normpath(os.path.join(target_dir, item))
		name = item
		size = os.path.getsize(item_path)
		is_dir = os.path.isdir(item_path)

		content_str = '\n'.join([content_str, f"- {name}: file_size={size} bytes, is_dir={is_dir}"])

	# strip() removes leading '\n'
	return content_str.strip()

	return f'Success: "{directory}" is within the working directory'