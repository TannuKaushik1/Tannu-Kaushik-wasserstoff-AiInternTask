# main.py
from fetch_emails import fetch_and_store_emails
from llm_utils import summarize_email, generate_reply
from database import init_db
from slack_notifier import send_slack_message

def run_assistant():
    init_db()
    fetch_and_store_emails()

    # Demo: Simulate summarizing and notifying
    import sqlite3
    conn = sqlite3.connect("emails.db")
    cursor = conn.cursor()
    cursor.execute("SELECT body FROM emails ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        body = row[0]
        summary = summarize_email(body)
        print("Summary:", summary)

        reply = generate_reply(body)
        print("\nSuggested Reply:\n", reply)

        send_slack_message(f"New important email:\n\nSummary: {summary}")
    else:
        print("No emails found.")

if __name__ == "__main__":
    run_assistant()
