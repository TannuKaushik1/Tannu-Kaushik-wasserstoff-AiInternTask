📬 AI Personal Email Assistant

An AI-powered personal email assistant that reads your Gmail inbox, understands email context using a Large Language Model (LLM), and interacts with tools like Slack, Google Calendar, and Web Search to help you draft replies, schedule events, or forward information.

## ✨ Features

- **Email Integration**: Read Gmail inbox and sent items using the Gmail API.
- **Context Understanding**: Use OpenAI GPT to summarize emails or determine intent.
- **Storage**: Store parsed email data in a local SQLite database with threading support.
- **Slack Integration**: Notify important emails to a Slack channel.
- **Calendar Integration**: Auto-schedule events by parsing email content.
- **Web Search**: Answer email queries with Google Search results.
- **Automated Replies**: Draft or auto-send replies based on LLM analysis.

## 🏗️ Architecture

[Gmail Inbox] → [Email Fetcher] → [SQLite DB] ↓ [LLM Processor] ↓ ┌────────────┬───────────────┬───────────────┐ ↓ ↓ ↓ ↓ [Reply Generator] [Slack Bot] [Google Calendar] [Web Search Tool] ↓ [Send Reply via Gmail]

bash
Copy
Edit

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-email-assistant.git
cd ai-email-assistant
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Configure Environment Variables
Create a .env file in the root directory with the following content:

ini
Copy
Edit
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
OPENAI_API_KEY=your-openai-api-key
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_CHANNEL_ID=your-slack-channel-id
GOOGLE_SEARCH_API_KEY=your-google-search-api-key
GOOGLE_SEARCH_ENGINE_ID=your-search-engine-id
4. Authenticate Gmail API
Follow the Gmail API Python Quickstart to create token.json and credentials.json:

Go to Gmail API Quickstart and follow the instructions to enable the Gmail API and download the credentials.

🚀 How to Run
After setting up the environment and configuring API credentials, run the following command to start the application:

bash
Copy
Edit
python main.py
This will:

Fetch unread emails from Gmail

Store them in the SQLite database

Use GPT to analyze emails and determine the next actions

Send a Slack message if an email is flagged as important

Schedule meetings or draft a reply using Google Calendar API and LLM

🧪 Example Usage
Email: "Can we schedule a call on Friday at 3PM?"

Action:

GPT parses the date/time

Creates a calendar event via Google Calendar API

Drafts a reply: "Sure, I've scheduled the meeting for Friday at 3PM. Here's the invite link."

📝 Folder Structure
css
Copy
Edit
src/
├── main.py
├── controllers/
│   └── email_controller.py
├── services/
│   ├── gmail_service.py
│   ├── slack_service.py
│   ├── calendar_service.py
│   ├── websearch_service.py
├── llm/
│   └── llm_handler.py
├── db/
│   └── database.py
├── utils/
│   └── helpers.py
.env
README.md
requirements.txt
📹 Demo Video
[link to demo video]

🤖 AI Development Notes
This project used GitHub Copilot and ChatGPT to generate boilerplate and integrate APIs efficiently. Prompt engineering was key in tuning GPT responses for summarizing emails and extracting actions.

📄 License
This project is licensed under the MIT License
