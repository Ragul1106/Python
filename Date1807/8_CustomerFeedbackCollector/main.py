from feedback_handler.collector import collect_feedback, show_feedback

feedback_db = {}

def main():
    while True:
        print("\n1. Collect Feedback\n2. Show All Feedback\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            customer_id = input("Enter Customer ID: ")
            feedback_text = input("Enter Feedback: ")
            cid = (customer_id.strip(),)
            collect_feedback(feedback_db, cid, feedback_text)

        elif choice == "2":
            show_feedback(feedback_db)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()