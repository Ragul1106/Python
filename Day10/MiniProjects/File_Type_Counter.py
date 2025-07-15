files = ["report.pdf", "data.xlsx", "image.jpg"]

file_types = {}
for file in files:
    ext = file.split(".")[-1]
    file_types[ext] = file_types.get(ext, 0) + 1

print("File counts:", file_types)