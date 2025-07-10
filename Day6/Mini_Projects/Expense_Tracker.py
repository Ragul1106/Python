def track_expenses(*expenses):
    expenses_list = list(expenses)
    total = sum(expenses_list)

    with_gst = list(map(lambda x: x * 1.18, expenses_list))
    
    return expenses_list, total, with_gst

expenses, total, with_gst = track_expenses(100, 200, 50)
print(f"Expenses: {expenses}")
print(f"Total: {total}")
print(f"With GST: {with_gst}")