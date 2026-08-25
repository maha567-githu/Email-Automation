import os
from dotenv import load_dotenv
import random
from email.message import EmailMessage
import smtplib
OTP=random.randint(100000,999999)
print(OTP)
load_dotenv()
sender_email=os.getenv("sender_email")
email_password=os.getenv("email_password")
receiver_email=input("enter reciver email")
message=EmailMessage()
message['Subject']="OTP VERIFICATION"
message['From']=email_password
message['TO']=receiver_email
message.set_content(f"HEY!\n Your OTP IS : {OTP}")
# Gmail server
server=smtplib.SMTP("smtp.gmail.com",587)
# SECURE CONNECTION
server.starttls()
# LOGIN
server.login(sender_email,email_password)
#SEND EMAIL
server.send_message(message)
# CLOSE SERVER
server.quit()
print("EMAIL SENT SUCCESSFULLY *")