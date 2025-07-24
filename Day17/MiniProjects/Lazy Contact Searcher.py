def contact_searcher(contacts):
    search_char = 'A'  
    while True:
        results = []
        for name, number in contacts.items():
            if name.startswith(search_char.upper()):
                results.append((name, number))
        new_char = yield results
        if new_char:
            search_char = new_char

contacts = {"Ragul": "555-1234", "Heera": "555-5678", "Ranjith": "555-9012"}
searcher = contact_searcher(contacts)
next(searcher)  

print(searcher.send('A'))  
print(searcher.send('H'))  