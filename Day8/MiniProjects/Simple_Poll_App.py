responses = []

def take_poll():
    question = "Do you support renewable energy? (Yes/No): "
    while True:
        response = input(question).capitalize()
        if response in ['Yes', 'No']:
            responses.append(response)
            break
        print("Invalid response")

def show_results():
    yes = responses.count('Yes')
    no = responses.count('No')
    print(f"\nResults: Yes - {yes}, No - {no}")

take_poll()
take_poll()
show_results()