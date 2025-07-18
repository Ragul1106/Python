from poll_utils.voting import cast_vote, show_results

voters = set()
poll_results = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
}

def main():
    while True:
        print("\n1. Vote\n2. View Results\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            voter_id = input("Enter Voter ID: ")
            vid = (voter_id.strip(),)
            if vid in voters:
                print("You have already voted!")
            else:
                print("Options: Option A, Option B, Option C")
                vote = input("Enter your vote: ")
                cast_vote(poll_results, vote.strip())
                voters.add(vid)

        elif choice == "2":
            show_results(poll_results)

        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
