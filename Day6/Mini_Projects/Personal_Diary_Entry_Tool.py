def diary_manager(entry):
    entries = []
    
    def save_entry():
        entries.append(entry)
        return len(entries)
    
    def get_stats():
        word_count = len(entry.split())
        return len(entry), word_count
    
    save_entry()
    return get_stats()

length, words = diary_manager("Today I learned about Python functions.")
print(f"Entry length: {length} chars, {words} words")