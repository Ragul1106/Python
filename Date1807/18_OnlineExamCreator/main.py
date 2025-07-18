from exam_creator.question_bank import add_question, view_questions, exam_bank

def main():
    while True:
        print("\n1. Add Question\n2. View All Questions\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            qid = input("Enter Question ID: ")
            question = input("Enter Question Text: ")
            options = input("Enter Options (comma-separated): ").split(',')
            answer = input("Enter Correct Answer: ")
            topics = input("Enter Topics (comma-separated): ").split(',')

            add_question(qid, question, options, answer, topics)

        elif choice == "2":
            view_questions()

        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()