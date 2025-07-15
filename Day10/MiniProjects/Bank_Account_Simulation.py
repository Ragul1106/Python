accounts = {}

def create_account(acc_no, name, balance=0):
    accounts[acc_no] = {"name": name, "balance": balance}

def low_balance_accounts():
    return {no: data for no, data in accounts.items() 
            if data["balance"] < 1000}

create_account(1001, "Ragul", 500)
print("Low balance:", low_balance_accounts())