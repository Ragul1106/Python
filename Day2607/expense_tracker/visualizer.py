import matplotlib.pyplot as plt

def show_pie_chart(summary):
    categories = summary.keys()
    amounts = summary.values()
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

def show_bar_chart(summary):
    categories = list(summary.keys())
    amounts = list(summary.values())
    plt.bar(categories, amounts, color="skyblue")
    plt.ylabel("Amount Spent")
    plt.title("Spending by Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
