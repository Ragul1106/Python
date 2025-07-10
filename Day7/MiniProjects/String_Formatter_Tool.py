name = "john doe".title()
salary = "50000.1234".replace(".1234", "")

formatted = "My name is %s and I earn ₹%.2f" % (name, float(salary))
print(formatted)