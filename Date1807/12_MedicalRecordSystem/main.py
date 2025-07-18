from healthcare_records.records import add_record, view_records

records = {}
illness_types = set()

def main():
    while True:
        print("\n1. Add Medical Record\n2. View All Records\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            illness = input("Enter Illness: ")

            patient_id = (pid.strip(),)
            add_record(records, patient_id, name, age, illness)
            illness_types.add(illness)

        elif choice == "2":
            view_records(records)
            print("\nIllness Types Encountered:", illness_types)

        elif choice == "3":
            break
        else:
            print("Invalid input. Try again.")
if __name__ == "__main__":
    main()
