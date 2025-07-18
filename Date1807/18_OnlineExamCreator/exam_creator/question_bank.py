exam_bank = {}

def add_question(qid, question, options, answer, topics):
    key = (qid.strip(),)
    if key in exam_bank:
        print("Question ID already exists.")
        return

    exam_bank[key] = {
        "question": question,
        "options": [opt.strip() for opt in options],
        "answer": answer.strip(),
        "topics": set(topic.strip().lower() for topic in topics)
    }
    print(f"Question '{qid}' added.")

def view_questions():
    if not exam_bank:
        print("No questions added yet.")
        return

    for qid, info in exam_bank.items():
        print(f"\nID: {qid[0]}")
        print(f"Q: {info['question']}")
        print(f"Options: {', '.join(info['options'])}")
        print(f"Answer: {info['answer']}")
        print(f"Topics: {', '.join(info['topics'])}")
