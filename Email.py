import smtplib
import ssl
from email.message import EmailMessage
from getpass4 import getpass

subject = "Email Using Python from my computer" 
body = "This is a test email created using Python!" # message
sender_email = input("Your email: ")
receiver_email = input("Receiver email: ") # email receiving the message
password = getpass('Password: ') # password using getpass to have a better security

message = EmailMessage() # start an email messager using the library
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1> 
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context() # Create a SSLContext object with default settings.

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server: # start a new instance
    server.login(sender_email, password) # loging in with autentification
    server.sendmail(sender_email, receiver_email, message.as_string()) # perform the email transaction

print("Success")