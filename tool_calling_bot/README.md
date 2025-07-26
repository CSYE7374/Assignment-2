
# Tool-Calling Chatbot

This is a Python-based chatbot that uses OpenAI's GPT model to perform tasks by calling external tools. The bot can:

- Perform basic math calculations
- Show current time in a given timezone
- Search the web using the DuckDuckGo API

This project was built for CSYE 7374 Assignment 2: Building Your First Tool-Calling Bot.

## Installation Instructions

1. Clone the repository:

    git clone https://github.com/your-username/tool-calling-bot.git
    cd tool-calling-bot

2. Create a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

    pip install -r requirements.txt

## How to Get Your OpenAI API Key

1. Go to https://platform.openai.com/account/api-keys
2. Create a new secret key and copy it
3. Set the key in your terminal:

    export OPENAI_API_KEY="your-api-key-here"

Alternatively, you can use a .env file if using python-dotenv.

## How to Run the Bot

Make sure your API key is set, then run:

    python main.py

The bot will start in your terminal and you can ask it questions. It will decide if it needs to use a tool and respond with the result.

## Example Conversations

Calculator:

    User: What is 25 * sqrt(16)?
    Bot: Result: 100.0

Time:

    User: What time is it in New York?
    Bot: 2025-07-24 14:05:00 (US/Eastern)

Web Search:

    User: Search for Python tutorials
    Bot: - Python Tutorial (https://realpython.com)
         - Learn Python (https://example.com)

Multi-tool:

    User: What time is it in Tokyo and what is 20% of 300?
    Bot: 2025-07-24 23:00:00 (Asia/Tokyo), Result: 60.0

## Known Limitations

- Web search results are limited and come from DuckDuckGo's Instant Answer API.
- Timezones must be valid, like "Asia/Tokyo" or "UTC".
- The calculator supports math functions like sqrt, sin, log from Python's math module.

## Project Structure

tool_calling_bot/
├── main.py             # Main chatbot logic
├── tools.py            # Tool implementations
├── config.py           # API key loading
├── requirements.txt    # Python dependencies
├── README.md           # Documentation

## Report and Demo

See report.pdf for details about the project.

The demo video link will be added in the README when available.
