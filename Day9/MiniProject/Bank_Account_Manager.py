accounts = [
    (1001, "Ragul", (5000.0, "active")),
    (1002, "Ranjith", (12000.5, "active")),
    (1003, "Arul", (750.25, "inactive"))
]

def show_account(acc_num):
    for account in accounts:
        num, name, (balance, status) = account  
        if num == acc_num:
            print(f"Account: {num}")
            print(f"Holder: {name}")
            print(f"Balance: ₹{balance:.2f}")
            print(f"Status: {status}\n")
            return
    print("Account not found")

show_account(1002)

try:
    accounts[0][2][0] = 6000.0
except TypeError:
    print("Cannot modify account data - tuples are immutable")