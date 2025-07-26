import shutil

def export_to_spreadsheet():
    try:
        shutil.copy("expenses.csv", "expense_export.csv")
        print("Exported to 'expense_export.csv'")
    except:
        print("No expenses to export.")
