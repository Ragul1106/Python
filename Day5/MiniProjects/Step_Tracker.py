total_steps = 0
days = 7
day = 1

while day <= days:
    steps = int(input(f"Day {day} steps: "))
    if steps == 0:
        print("No steps recorded")
        continue
    total_steps += steps
    day += 1
else:
    avg_steps = total_steps / days
    print(f"\nTotal steps: {total_steps}")
    print(f"Average daily steps: {avg_steps:.0f}")