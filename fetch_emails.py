# fetch_emails.py

from authenticate import authenticate_gmail
from googleapiclient.errors import HttpError

def fetch_emails():
    try:
        # Get the Gmail API service using the authenticate function
        service = authenticate_gmail()

        # Get the list of emails from Gmail
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()

        # Get the email list
        messages = results.get('messages', [])

        if not messages:
            print('No new messages.')
        else:
            print('Messages:')
            for message in messages[:10]:  # Only fetch the first 10 unread emails
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                print(f"Snippet: {msg['snippet']}")

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    fetch_emails()
