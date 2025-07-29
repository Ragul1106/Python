import os
import difflib

def load_documents(directory):
    documents = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    if not content:
                        raise ValueError(f"{filename} is empty!")
                    documents.append((filename, content))
    except Exception as e:
        print(f"Error loading documents: {e}")
    return documents

def compare_documents(documents, threshold=0.7):
    checked = set()
    for i, (name1, text1) in enumerate(documents):
        for j, (name2, text2) in enumerate(documents):
            if i != j and (name2, name1) not in checked:
                similarity = difflib.SequenceMatcher(None, text1, text2).ratio()
                if similarity >= threshold:
                    yield (name1, name2, round(similarity * 100, 2))
                checked.add((name1, name2))

def main():
    folder_path = input("Enter the folder path with .txt files: ")
    if not os.path.isdir(folder_path):
        print("Invalid directory path.")
        return

    documents = load_documents(folder_path)
    if len(documents) < 2:
        print("Need at least 2 non-empty documents to check for plagiarism.")
        return

    print("\nPossible Plagiarism Detected:\n")
    found = False
    for name1, name2, score in compare_documents(documents):
        print(f"{name1} <--> {name2}: {score}% match")
        found = True

    if not found:
        print("No significant matches found.")

if __name__ == "__main__":
    main()
