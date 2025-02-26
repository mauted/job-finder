import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

def send_notification(subject, body, to_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'your_email@example.com'
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        # Send email through SMTP
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login('your_email@example.com', 'your_password')  # Use environment variables or safer methods for credentials
            server.sendmail(msg['From'], msg['To'], msg.as_string())

        logging.info(f"Notification sent to {to_email}")
    except Exception as e:
        logging.error(f"Error sending notification: {e}")
