def authenticate_gmail():
    creds = None
    token_path = r'C:\Users\Tannu Kaushik\Downloads\ai_email_assistant\backend\token.json'

    # Check if token.json exists
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Use the manual authorization flow
            flow = InstalledAppFlow.from_client_secrets_file(
                r'C:\Users\Tannu Kaushik\Downloads\ai_email_assistant\backend\credentials.json',  # Full path to credentials.json
                SCOPES
            )
            # Instead of running the local server, use manual authorization
            creds = flow.run_console()

        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds


