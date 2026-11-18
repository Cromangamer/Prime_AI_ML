# Modes of File Operations in Python

# 'r' - Read mode (default):
# Opens an existing file for reading. Raises FileNotFoundError if the file does not exist.

# 'w' - Write mode:
# Opens a file for writing. Creates the file if it does not exist and deletes all existing content.

# 'x' - Exclusive create mode:
# Creates a new file for writing. Raises FileExistsError if the file already exists.

# 'a' - Append mode:
# Opens a file for writing at the end. Creates the file if it does not exist; existing content is preserved.

# 't' - Text mode (default):
# Opens the file as text. Python automatically handles text encoding and newline conversion.

# 'b' - Binary mode:
# Opens the file as raw bytes. Use it for images, audio, PDFs, or other non-text data.

# 'r+' - Read and write mode:
# Opens an existing file for both reading and writing. The file pointer starts at the beginning.

# 'w+' - Write and read mode:
# Opens a file for both reading and writing. Creates it if needed, but erases existing content.

# 'a+' - Append and read mode:
# Opens a file for both reading and appending. Creates it if needed; writes always go to the end.

# 'x+' - Exclusive create and read/write mode:
# Creates a new file for both reading and writing. Raises FileExistsError if the file already exists.

# '+' - Update mode modifier:
# '+' is used with 'r', 'w', 'a', or 'x' to allow both reading and writing.
# It does not work alone and does not overwrite a file by itself.

# Common text mode combinations:
# 'rt' - Read text (same as 'r').
# 'wt' - Write text (same as 'w').
# 'xt' - Exclusive-create text (same as 'x').
# 'at' - Append text (same as 'a').
# 'r+t' or 'rt+' - Read and write existing text file.
# 'w+t' or 'wt+' - Write and read text file, deleting existing content.
# 'x+t' or 'xt+' - Exclusive-create text file for reading and writing.
# 'a+t' or 'at+' - Append and read text file.

# Common binary mode combinations:
# 'rb' - Read binary data.
# 'wb' - Write binary data, deleting existing content.
# 'xb' - Exclusive-create binary file.
# 'ab' - Append binary data.
# 'r+b' or 'rb+' - Read and write existing binary file.
# 'w+b' or 'wb+' - Write and read binary file, deleting existing content.
# 'x+b' or 'xb+' - Exclusive-create binary file for reading and writing.
# 'a+b' or 'ab+' - Append and read binary file.
