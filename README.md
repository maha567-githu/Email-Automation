# Email OTP Automation

Python automation project that generates a 6-digit OTP and sends it automatically to a receiver's email using Gmail SMTP.

## Features

- Generates a random 6-digit OTP
- Takes receiver email as input
- Sends OTP automatically
- Uses Gmail SMTP
- Keeps email credentials secure using environment variables

## Technologies Used

- Python
- smtplib
- email.message
- random
- python-dotenv

## How It Works

1. Generates a random 6-digit OTP.
2. Takes the receiver's email address.
3. Connects to Gmail SMTP server.
4. Establishes a secure TLS connection.
5. Authenticates the sender.
6. Sends the OTP.
7. Closes the SMTP connection.

## Setup

Install the required library:

```bash
pip install python-dotenv
Create a .env file in the project folder:

sender_email=your-email@gmail.com
email_password=your-app-password

Do not upload the .env file to GitHub.

Run
python send_email.py
Security

Email credentials are stored in environment variables instead of being hardcoded in the Python source code.

The .env file should never be uploaded to GitHub.

Project Purpose

This project demonstrates Python automation, SMTP email handling, OTP generation, and secure credential management.
