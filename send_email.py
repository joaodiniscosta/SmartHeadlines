import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, html_content):
    """
    Sends an HTML email using Gmail's SMTP server.
    Arguments:
        subject (str): The email subject line.
        html_content (str): The HTML string containing the email body.
    """
    
    # --- Configuration ---
    host = "smtp.gmail.com"
    port = 465
    
    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")
    
    if not username or not password or not receiver:
        print("Error: Email credentials are missing from environment variables.")
        return

    # Create the email object
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = username
    message["To"] = receiver

    # Convert the HTML string into a MIME object and attach it
    part = MIMEText(html_content, "html")
    message.attach(part)

    # Context for security
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message.as_string())
            print("HTML Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")