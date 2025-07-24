def id_generator(prefix="TRX"):
    count = 1
    while True:
        reset_value = yield f"{prefix}{count:03d}"
        if reset_value is not None:
            count = reset_value
        count += 1
        if count > 1000: 
            raise StopIteration("Reached max IDs")

gen = id_generator()
next(gen)  
for _ in range(5):
    print(next(gen))
gen.send(50)  
print(next(gen))  