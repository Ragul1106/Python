import math
from functools import wraps

def radians_to_degrees(func):
    @wraps(func)
    def wrapper(x):
        result = func(x)
        return f"{math.degrees(x)}° → {result}"
    return wrapper

@radians_to_degrees
def calc_sin(x):
    return math.sin(x)

@radians_to_degrees
def calc_cos(x):
    return math.cos(x)

@radians_to_degrees
def calc_tan(x):
    return math.tan(x)

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("Type 'exit' to quit")
    print("Available functions: +, -, *, /, sin, cos, tan, log, sqrt, pow")

    while True:
        try:
            expr = input("Enter expression: ").strip().lower()
            if expr == 'exit':
                print("Exiting calculator.")
                break

            if expr.startswith("sin"):
                val = float(expr.split("sin")[1])
                print("Result:", calc_sin(math.radians(val)))
            elif expr.startswith("cos"):
                val = float(expr.split("cos")[1])
                print("Result:", calc_cos(math.radians(val)))
            elif expr.startswith("tan"):
                val = float(expr.split("tan")[1])
                print("Result:", calc_tan(math.radians(val)))
        
            elif expr.startswith("log"):
                val = float(expr.split("log")[1])
                print("Result:", math.log(val))
           
            elif expr.startswith("sqrt"):
                val = float(expr.split("sqrt")[1])
                print("Result:", math.sqrt(val))
            
            elif "pow" in expr:
                base, exp = expr.split("pow")[1].split(",")
                print("Result:", math.pow(float(base), float(exp)))
           
            else:
                print("Result:", eval(expr))

        except ZeroDivisionError:
            print("❌ Error: Division by zero.")
        except ValueError:
            print("❌ Error: Invalid number or format.")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    scientific_calculator()
