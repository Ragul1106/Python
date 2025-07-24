def calculation_engine(operations):
    for a, b, op in operations:
        if op == '+':
            yield a + b
        elif op == '-':
            yield a - b
        elif op == '*':
            yield a * b
        elif op == '/':
            yield a / b if b != 0 else float('nan')

ops = [(10, 5, '+'), (8, 3, '-'), (4, 7, '*'), (9, 3, '/')]
engine = calculation_engine(ops)

for result in engine:
    print(f"Result: {result}")