import smtplib
import time
from email.message import EmailMessage
import os

def retry(retries=3, delay=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[Attempt {attempt+1}] Failed: {e}")
                    time.sleep(delay)
            print("All retry attempts failed.")
        return wrapper
    return decorator

class Email:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password
        self.msg = EmailMessage()

    def set_content(self, subject, body, to):
        self.msg['Subject'] = subject
        self.msg['From'] = self.sender
        self.msg['To'] = to
        self.msg.set_content(body)

    def attach_file(self, filepath):
        try:
            with open(filepath, 'rb') as f:
                file_data = f.read()
                file_name = os.path.basename(filepath)
                self.msg.add_attachment(file_data,
                                        maintype='application',
                                        subtype='octet-stream',
                                        filename=file_name)
        except FileNotFoundError:
            print(f"Attachment not found: {filepath}")

    @retry(retries=3, delay=3)
    def send(self, smtp_server='smtp.gmail.com', port=587):
        try:
            with smtplib.SMTP(smtp_server, port) as smtp:
                smtp.starttls()
                smtp.login(self.sender, self.password)
                smtp.send_message(self.msg)
                print("Email sent successfully!")
        except smtplib.SMTPException as e:
            raise Exception(f"SMTP error: {e}")


if __name__ == "__main__":
    sender_email = input("Your Email: ")
    password = input("App Password or Email Password: ")
    recipient = input("Recipient Email: ")

    name = input("Recipient Name: ")
    subject = "Welcome to Our Newsletter"
    body_template = f"""
    Hello {name},

    Thank you for subscribing to our newsletter!
    Stay tuned for exciting updates.

    Regards,
    Team
    """

    email = Email(sender_email, password)
    email.set_content(subject, body_template, recipient)

    file_path = input("Attachment file path (or press enter to skip): ").strip()
    if file_path:
        email.attach_file(file_path)

    email.send()
