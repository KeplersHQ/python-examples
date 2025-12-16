import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_base_url = os.getenv('API_BASE_URL')
api_key = os.getenv('API_KEY')

session = requests.Session()
session.headers.update({
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
})

def send_instant_email():
    try:
        response = session.post(
            f'{api_base_url}/send-email/instant',
            json={
                'to': [os.getenv('TO_EMAIL')],
                'subject': f'Welcome {os.getenv("USER_NAME")}!',
                'body': f'<h1>Welcome {os.getenv("USER_NAME")}!</h1><p>Thank you for joining our platform.</p>',
                'is_html': True
            }
        )

        response.raise_for_status()

        print('Email sent successfully!')
        print('Response:', response.json())
    except requests.exceptions.HTTPError as error:
        print('Error sending email:')
        print('Status:', error.response.status_code)
        print('Data:', error.response.json())
    except Exception as error:
        print('Error sending email:', str(error))

def main():
    print('=== Sending Simple Email ===')
    send_instant_email()

if __name__ == '__main__':
    main()
