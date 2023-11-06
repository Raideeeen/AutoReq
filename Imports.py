import os
import pkgutil
import argparse
import ast

standard_library_modules = set(module[1] for module in pkgutil.iter_modules())


def is_standard_library_module(module_name):
	return module_name in standard_library_modules


def get_imports_from_file(file_path, all_imports):
	with open(file_path, "r", encoding="utf-8") as file:
		code = file.read()

		try:
			tree = ast.parse(code)
		except SyntaxError:
			print(f"SyntaxError in file: {file_path}")
			return

		for node in ast.walk(tree):
			if isinstance(node, ast.Import):
				for name in node.names:
					module_name = name.name.split(".")[0]
					if is_standard_library_module(module_name):
						all_imports.add(module_name)
			elif isinstance(node, ast.ImportFrom):
				if node.module is not None:
					module_name = node.module.split(".")[0]
					if is_standard_library_module(module_name):
						all_imports.add(module_name)


def process_directory(directory_path, output):
	all_imports = set()

	if not os.path.exists(directory_path):
		print(f"Directory '{directory_path}' does not exist.")
		return

	if os.path.isfile(directory_path):
		get_imports_from_file(directory_path, all_imports)
	else:
		for root, _, files in os.walk(directory_path):
			for file in files:
				if file.endswith(".py"):
					file_path = os.path.join(root, file)
					get_imports_from_file(file_path, all_imports)

	print("Imported modules:")
	for module in all_imports:
		print(module)

	if output:
		with open(output, "w") as fp:
			for module in all_imports:
				fp.write(module + "\n")


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Python Import Scanner")
	parser.add_argument("path", help="File path or directory path")
	parser.add_argument("--output", help="Output the imported module lists to a file", required=False)

	args = parser.parse_args()

	process_directory(args.path, args.output)
