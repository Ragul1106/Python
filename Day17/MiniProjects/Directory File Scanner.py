import os

def file_scanner(root, max_files=100, extension=".txt"):
    count = 0
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(extension):
                yield os.path.join(dirpath, filename)
                count += 1
                if count >= max_files:
                    raise StopIteration(f"Reached max files: {max_files}")


# for filepath in file_scanner('/path/to/directory', max_files=10):
#     print(filepath)