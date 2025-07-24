def csv_reader(filename):
    with open(filename, 'r') as file:
        header = next(file)  
        for line in file:
            cleaned = line.strip()
            if cleaned == "END":
                raise StopIteration("END marker found")
            yield cleaned.split(',')

# Example usage (create test.csv first):
# for row in csv_reader('test.csv'):
#     print(row)