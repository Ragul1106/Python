read = 1
write = 2
execute = 4

user_permission = int(input("Enter your permission level (1-7): "))

print("\nYour permissions:")
if user_permission & read:
    print("- Read access")
if user_permission & write:
    print("- Write access")
if user_permission & execute:
    print("- Execute access")