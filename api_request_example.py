import base64
import os
import pickle
import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API setup
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Infobip API setup
INFOBIP_API_KEY = '007edef130cd2889d235a3e0a2e65009-4af9d3a6-3dd0-43a7-aff3-8e28df62b842'
INFOBIP_BASE_URL = 'https://l3y3n2.api.infobip.com'
TO_WHATSAPP_NUMBER = '9076421921'
FROM_WHATSAPP_NUMBER = '7977282697'

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    service = build('gmail', 'v1', credentials=creds)
    return service

def get_latest_email(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
    messages = results.get('messages', [])
    if not messages:
        return None
    msg = service.users().messages().get(userId='me', id=messages[0]['id']).execute()
    return msg

def extract_email_details(msg):
    payload = msg['payload']
    headers = payload['headers']
    subject = next(header['value'] for header in headers if header['name'] == 'Subject')
    from_ = next(header['value'] for header in headers if header['name'] == 'From')
    parts = payload.get('parts', [])
    body = ''
    if parts:
        body = base64.urlsafe_b64decode(parts[0]['body']['data']).decode('utf-8')
    return from_, subject, body

def send_whatsapp_message(from_, subject, body):
    url = f"{INFOBIP_BASE_URL}/whatsapp/1/message/text"
    headers = {
        'Authorization': f'App {INFOBIP_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "from": FROM_WHATSAPP_NUMBER,
        "to": TO_WHATSAPP_NUMBER,
        "content": {
            "text": f"New Email:\nFrom: {from_}\nSubject: {subject}\nBody: {body}"
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code, response.json()

def main():
    service = get_gmail_service()
    msg = get_latest_email(service)
    if msg:
        from_, subject, body = extract_email_details(msg)
        status_code, response = send_whatsapp_message(from_, subject, body)
        if status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message: {response}")

if __name__ == '__main__':
    main()
