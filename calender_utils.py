# calendar_utils.py
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os

def create_calendar_event(summary, start_time, end_time):
    creds = Credentials.from_authorized_user_file("token.json")
    service = build("calendar", "v3", credentials=creds)

    event = {
        "summary": summary,
        "start": {"dateTime": start_time, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end_time, "timeZone": "Asia/Kolkata"},
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    return event.get("htmlLink")
