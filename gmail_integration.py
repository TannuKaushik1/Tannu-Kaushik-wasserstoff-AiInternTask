import base64
from googleapiclient.discovery import build

# Function to fetch the latest unread email
def get_latest_email(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("No new messages.")
        return None
    
    # Get the first unread message
    message_id = messages[0]['id']
    email_content = get_email_data(service, message_id)
    
    return email_content

# Helper function to extract email content
def get_email_data(service, message_id):
    try:
        message = service.users().messages().get(userId='me', id=message_id).execute()
        
        # Extract and decode the email content (base64 encoded)
        msg_data = message['payload']['headers']
        email_body = message['payload']['body']['data']
        decoded_body = base64.urlsafe_b64decode(email_body).decode('utf-8')
        
        return decoded_body
    except Exception as error:
        print(f"An error occurred: {error}")
        return None
