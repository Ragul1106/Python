polls = {}

def create_poll():
    question = input("Enter poll question: ")
    options = input("Enter options (comma separated): ").split(',')
    polls[question] = {opt.strip(): 0 for opt in options}
    print("Poll created!")

def take_poll():
    if not polls:
        print("No polls available")
        return
    
    print("\nAvailable Polls:")
    for i, q in enumerate(polls.keys(), 1):
        print(f"{i}. {q}")
    
    try:
        choice = int(input("Select poll: ")) - 1
        question = list(polls.keys())[choice]
        options = polls[question]
        
        print(f"\n{question}")
        for i, opt in enumerate(options.keys(), 1):
            print(f"{i}. {opt}")
        
        vote = int(input("Your vote: ")) - 1
        option = list(options.keys())[vote]
        polls[question][option] += 1
        print("Vote recorded!")
    except (ValueError, IndexError):
        print("Invalid selection")

def show_results():
    if not polls:
        print("No polls available")
        return
    
    for question, options in polls.items():
        print(f"\n{question}")
        for opt, count in options.items():
            print(f"{opt}: {count} votes")

while True:
    print("\n1. Create Poll\n2. Take Poll\n3. Show Results\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        create_poll()
    elif choice == '2':
        take_poll()
    elif choice == '3':
        show_results()
    elif choice == '4':
        break
    else:
        print("Invalid choice")