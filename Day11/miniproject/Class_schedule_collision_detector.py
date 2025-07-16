math_class = {'Mon 9AM', 'Wed 9AM'}
physics_class = {'Mon 9AM', 'Fri 11AM'}

conflicts = math_class & physics_class
print("Schedule conflicts:", conflicts)