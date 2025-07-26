import csv

def export_to_csv(contacts, filename="contacts_export.csv"):
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "category"])
        writer.writeheader()
        for c in contacts:
            writer.writerow(c.to_dict())
