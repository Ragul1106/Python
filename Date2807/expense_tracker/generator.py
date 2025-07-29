from datetime import datetime

def expense_generator(expenses, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    for e in expenses:
        date = datetime.strptime(e['date'], "%Y-%m-%d")
        if start <= date <= end:
            yield e
