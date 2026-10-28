import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
	try:
		abs_working_dir = os.path.abspath(working_directory)
		abs_target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

		# Check if target dir is within the working directory
		if os.path.commonpath([abs_working_dir, abs_target_dir]) != abs_working_dir:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

		# check that target dir is a dir
		if not os.path.isdir(abs_target_dir):
			return f'Error: "{directory}" is not a directory'

		# collect all items in provided directory
		content_str = ""
		for item in os.listdir(abs_target_dir):
			item_path = os.path.normpath(os.path.join(abs_target_dir, item))
			name = item
			size = os.path.getsize(item_path)
			is_dir = os.path.isdir(item_path)

			content_str = '\n'.join([content_str, f"- {name}: file_size={size} bytes, is_dir={is_dir}"])

		# strip() removes leading '\n'
		return content_str.strip()

	except Exception as e:
		return f"Error: listing files: {e}"