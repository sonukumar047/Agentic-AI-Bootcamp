# -----------------------------------------
# 1. Opening a File
# open(filename, mode)
# Modes: 'r' = read, 'w' = write, 'a' = append, 'x' = create, 'b' = binary, 't' = text (default)
# -----------------------------------------

# Writing to a file (creates if not exists)
with open("example.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a file write example.\n")

# -----------------------------------------
# 2. Reading a File
# -----------------------------------------

# Read entire content
with open("example.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# Read line by line
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())

# Read as list of lines
with open("example.txt", "r") as f:
    lines = f.readlines()
    print("Lines as list:", lines)

# -----------------------------------------
# 3. Appending to a File
# -----------------------------------------
with open("example.txt", "a") as f:
    f.write("Appending this line.\n")

# -----------------------------------------
# 4. Reading After Append
# -----------------------------------------
with open("example.txt", "r") as f:
    print("After append:\n", f.read())

# -----------------------------------------
# 5. Using try-except with file
# -----------------------------------------
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")

# -----------------------------------------
# 6. Writing a List of Lines
# -----------------------------------------
lines = ["Python\n", "File\n", "Write\n"]
with open("list_write.txt", "w") as f:
    f.writelines(lines)

# -----------------------------------------
# 7. Reading & Writing in Binary Mode (Advanced)
# -----------------------------------------
# Writing binary
with open("binary_file.bin", "wb") as bf:
    bf.write(b"This is binary content")

# Reading binary
with open("binary_file.bin", "rb") as bf:
    data = bf.read()
    print("Binary content:", data)

# -----------------------------------------
# Summary:
# - Use `open()` with `r`, `w`, `a`, `b`, `x` modes.
# - Always use `with open()` → handles automatic closing.
# - Use `.read()`, `.readlines()`, `.write()`, `.writelines()`.
# - Handle errors with `try-except`.
# -----------------------------------------
