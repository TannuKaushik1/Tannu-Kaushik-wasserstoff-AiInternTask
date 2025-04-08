# backend/db.py

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("emails.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table to store emails
cursor.execute("""
CREATE TABLE IF NOT EXISTS emails (
    id TEXT PRIMARY KEY,
    thread_id TEXT,
    sender TEXT,
    recipient TEXT,
    subject TEXT,
    timestamp TEXT,
    snippet TEXT,
    body TEXT
)
""")

conn.commit()

# Function to save email to the database
def save_email(email_data):
    cursor.execute("""
        INSERT OR REPLACE INTO emails (id, thread_id, sender, recipient, subject, timestamp, snippet, body)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        email_data["id"],
        email_data["thread_id"],
        email_data["sender"],
        email_data["recipient"],
        email_data["subject"],
        email_data["timestamp"],
        email_data["snippet"],
        email_data["body"]
    ))
    conn.commit()

# Function to retrieve emails (for LLM context)
def get_recent_emails(limit=10):
    cursor.execute("SELECT * FROM emails ORDER BY timestamp DESC LIMIT ?", (limit,))
    return cursor.fetchall()
