import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


load_dotenv()


def send_email(msg_subject, body):

    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_USERNAME')
    msg['To'] = os.getenv('EMAIL_USERNAME')
    msg['Subject'] = msg_subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Replace with your SMTP server details
        server.starttls()
        server.login(os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD'))
        server.sendmail(os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_USERNAME'), msg.as_string())
