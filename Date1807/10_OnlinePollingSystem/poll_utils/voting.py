def cast_vote(results, vote):
    if vote in results:
        results[vote] += 1
        print(f"Vote for {vote} recorded!")
    else:
        print("Invalid option!")

def show_results(results):
    print("\nPoll Results:")
    for option, count in results.items():
        print(f"{option}: {count} votes")

    total_votes = sum(results.values())
    print(f"Total votes: {total_votes}")