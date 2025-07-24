def email_sender(email_list):
    sent = 0
    batch_size = 5
    try:
        while sent < len(email_list):
            batch = email_list[sent:sent+batch_size]
            for email in batch:
                try:
                    yield f"Sending to {email}"
                    sent += 1
                except Exception as e:
                    yield f"Failed to send to {email}: {str(e)}"

            new_size = yield f"Batch complete. {sent}/{len(email_list)} sent"
            if new_size is not None:
                batch_size = new_size
    finally:
        return f"Completed: {sent} emails sent"

emails = [f"user{i}@example.com" for i in range(1, 13)]
sender = email_sender(emails)
next(sender)  

while True:
    try:
        status = sender.send(3)  
        print(status)
    except StopIteration as e:
        print(e.value)
        break