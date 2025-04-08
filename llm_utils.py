# llm_utils.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_email(body):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize the following email:\n\n{body}"}]
    )
    return response.choices[0].message.content.strip()

def generate_reply(body):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Write a polite email reply to this message:\n\n{body}"}]
    )
    return response.choices[0].message.content.strip()
