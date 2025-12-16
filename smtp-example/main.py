import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

smtp_host = os.getenv('SMTP_HOST')
smtp_port = int(os.getenv('SMTP_PORT'))
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')
from_email = os.getenv('FROM_EMAIL')
to_email = os.getenv('TO_EMAIL')

def send_email():
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = 'Test Email from Keplers SMTP'

        text_part = MIMEText('This is a test email sent via Keplers.email SMTP service.', 'plain')
        html_part = MIMEText('<p>This is a <strong>test email</strong> sent via Keplers.email SMTP service.</p>', 'html')

        msg.attach(text_part)
        msg.attach(html_part)

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        print('Email sent successfully!')
        print(f'Message sent from: {from_email}')
        print(f'Message sent to: {to_email}')
    except Exception as error:
        print('Error sending email:', str(error))

if __name__ == '__main__':
    send_email()
