def calculate_bill(*units):
    total = 0
    for unit in units:
        if unit <= 100:
            total += unit * 3
        elif unit <= 200:
            total += 100*3 + (unit-100)*5
        else:
            total += 100*3 + 100*5 + (unit-200)*7

    add_gst = lambda x: x * 1.18
    return add_gst(total)

print(f"Total bill with GST: ₹{calculate_bill(150, 250):.2f}")