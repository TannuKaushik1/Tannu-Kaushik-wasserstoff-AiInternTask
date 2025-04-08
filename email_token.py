from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import os
import pickle

# The API scope we are requesting.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    
    # If modifying the Gmail API permissions, delete the token.pickle file.
    token_path = 'token.json'  # Path where token will be saved

    # Check if the token file exists, if not, we run the authorization flow.
    if os.path.exists(token_path):
        print("Token found, loading...")
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    else:
        # No token found, proceed with authorization flow
        print("No token found, starting authorization flow...")

        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)  # Path to your credentials.json
        creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)
        
    return creds

# Running the authentication flow and saving token.json
if __name__ == '__main__':
    creds = authenticate_gmail()
    print("Gmail authentication successful!")
