# -----------------------------------------
# 1. Using os.path
# -----------------------------------------
import os

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Create an absolute path
abs_path = os.path.abspath("example.txt")
print("Absolute Path of 'example.txt':", abs_path)

# Join paths (cross-platform safe)
joined_path = os.path.join(cwd, "folder", "myfile.txt")
print("Joined Path:", joined_path)

# Check if file exists
print("Does example.txt exist?", os.path.exists("example.txt"))

# Get file name and directory
print("File name:", os.path.basename(abs_path))
print("Directory name:", os.path.dirname(abs_path))

# -----------------------------------------
# 2. Using pathlib (modern & recommended)
# -----------------------------------------
from pathlib import Path

# Get current path
current_path = Path.cwd()
print("Pathlib - Current Path:", current_path)

# Create file path using /
file_path = current_path / "folder" / "data.txt"
print("Pathlib - Constructed Path:", file_path)

# Check file existence
print("Pathlib - Does file exist?", file_path.exists())

# Get parent directory and filename
print("Parent directory:", file_path.parent)
print("File name:", file_path.name)

# -----------------------------------------
# 3. Reading a file using pathlib
# -----------------------------------------
text_file = Path("example.txt")
if text_file.exists():
    content = text_file.read_text()
    print("File Content:\n", content)
else:
    print("example.txt does not exist.")

# -----------------------------------------
# 4. Writing a file using pathlib
# -----------------------------------------
new_file = Path("output.txt")
new_file.write_text("Created using pathlib!\nPython makes it easy.")

# -----------------------------------------
# 5. Creating directories (if not exists)
# -----------------------------------------
output_folder = Path("results")
output_folder.mkdir(exist_ok=True)
print("Created 'results' folder (if not already there)")

# -----------------------------------------
# Summary:
# - `os.path` is older, still widely used.
# - `pathlib` is newer and more readable using `/` operator.
# - Use absolute/relative paths safely with `Path()` or `os.path`.
# -----------------------------------------
