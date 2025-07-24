class TemperatureFilter:
    def __init__(self, filename, min_temp):
        self.file = open(filename)
        self.min_temp = min_temp
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while True:
            line = next(self.file)
            temp = float(line.strip())
            if temp > self.min_temp:
                return temp

with open('temps.txt', 'w') as f:
    f.write("25.5\n31.2\n28.7\n32.1\n29.8\n")
print("\nTemperature Filter:")
for temp in TemperatureFilter('temps.txt', 30):
    print(f"High temperature: {temp}°C")