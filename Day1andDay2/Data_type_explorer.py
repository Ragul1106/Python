value = input("Enter any value: ")
print(f"\nValue: {value}")
print(f"Type: {type(value)}")

convert = input("\nConvert to (int/float/bool/str/none)? ").lower()
if convert == 'int':
    try:
        new_value = int(value)
        print(f"Converted to int: {new_value}")
    except ValueError:
        print("Cannot convert to int")
elif convert == 'float':
    try:
        new_value = float(value)
        print(f"Converted to float: {new_value}")
    except ValueError:
        print("Cannot convert to float")
elif convert == 'bool':
    new_value = bool(value)
    print(f"Converted to bool: {new_value}")
elif convert == 'str':
    new_value = str(value)
    print(f"Converted to str: {new_value}")
else:
    print("No conversion performed")

if convert in ['int', 'float', 'bool', 'str']:
    print(f"New type: {type(new_value)}")