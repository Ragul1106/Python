def format_chat(*messages):
    format_msg = lambda m: f"[10:30] {m.upper()}"
    return list(map(format_msg, messages))

print(format_chat("hello", "how are you?", "goodbye"))