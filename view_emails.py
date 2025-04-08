# backend/view_emails.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "emails.db")

def view_emails():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()

    for row in rows:
        print("ID:", row[0])
        print("From:", row[1])
        print("To:", row[2])
        print("Subject:", row[3])
        print("Time:", row[4])
        print("Body:", row[5])
        print("="*40)

    conn.close()

if __name__ == "__main__":
    view_emails()
