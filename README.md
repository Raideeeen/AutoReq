# AutoReq: Python Dependency Scanner

AutoReq is a Python script that simplifies the process of managing Python dependencies by automatically generating a `requirements.txt` file.

## Features
- **Automated Dependency Scanning:** AutoReq scans your Python codebase to detect all imported modules.
- **Auto-Generated `requirements.txt`:** It generates a `requirements.txt` file with the list of dependencies.
- **Local Library Handling:** AutoReq recognizes and excludes local library modules, keeping your requirements clean.
- **Directory or File Scanning:** You can use AutoReq to scan both directories and individual Python files.

## Usage
1. Clone or download this repository.
2. Run the script, providing the file path or directory path you want to scan.
3. Optionally, specify the `--output` parameter to save the imported module list to a file.

### For Scanning Directories
```bash
python Imports.py path/to/your/directory --output requirements.txt
```

### For Scanning Files
```bash
python Imports.py path/to/your/file --output requirements.txt
```
