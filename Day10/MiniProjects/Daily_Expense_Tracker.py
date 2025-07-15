expenses = {}

def add_expense(date, category, amount):
    expenses.setdefault(date, {}).update({category: amount})

def daily_total(date):
    return sum(expenses.get(date, {}).values())

def high_spending_days(threshold=500):
    return {date: total for date in expenses 
            if (total := sum(expenses[date].values())) > threshold}

add_expense("2023-05-01", "food", 300)
add_expense("2023-05-01", "transport", 200)
print("High spending days:", high_spending_days())