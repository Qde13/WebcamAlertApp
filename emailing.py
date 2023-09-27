import smtplib
import os
from email.message import EmailMessage
import imghdr

password = os.getenv("PASSWORD")
sender = "zemka.kit@gmail.com"
receiver = "zemka.kit@gmail.com"


def send_email(image_path):
    print("Email send started")
    email_message = EmailMessage()
    email_message["Subject"] = "New object detected!"
    email_message.set_content("Hey, we just saw a new object!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()
    print("email send ended")

if __name__ == "__main__":
    send_email(image_path="images/15.png")


