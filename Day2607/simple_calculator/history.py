history_list = []

def add_history(expression, result):
    history_list.append((expression, result))

def show_history():
    if not history_list:
        print("No history available.")
        return
    for idx, (expr, res) in enumerate(history_list, 1):
        print(f"{idx}. {expr} = {res}")
