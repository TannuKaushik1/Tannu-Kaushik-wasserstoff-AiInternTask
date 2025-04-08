import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure to store this securely!

def get_email_summary(email_content):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can use other engines if preferred
        prompt=f"Summarize the following email:\n{email_content}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def generate_reply(email_content):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a friendly and professional reply to the following email:\n{email_content}",
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
