def reverse_line_reader(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()[::-1]

# for reversed_line in reverse_line_reader('data.txt'):
#     print(reversed_line)