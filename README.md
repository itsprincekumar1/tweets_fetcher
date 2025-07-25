# 🐦 Tweets Fetcher CLI Tool

A simple Python command-line tool that allows you to **fetch the latest tweet from any public X (Twitter) account** using the X API v2 (Free Tier).  
Built with `tweepy`, `click`, and some CLI magic 🧙‍♂️

---

## 🚀 Features

- ✅ Fetches the **most recent tweet** from any public X username.
- ✅ CLI-based — no GUI or browser needed.
- ✅ Modular and scalable structure.
- ✅ Uses environment variables for secure API key handling.

---

## 📁 Project Structure

```text
tweets-fetcher/
├── cli/
│   └── user_cli.py           # CLI entrypoint using Click
├── config/
│   └── credentials.py        # Loads the BEARER_TOKEN
├── core/
│   └── user_fetcher.py       # Fetch logic for recent tweet
├── .env                      # Stores secret keys (not pushed to GitHub)
├── main.py                   # Entry point for CLI
├── requirements.txt
└── README.md


---
```

## 🧠 Prerequisites

- Python 3.8 or above
- A Twitter/X Developer Account (Free Tier is enough)
- Git installed

---

## 🔐 Getting Your Bearer Token (X API v2)

1. Visit: [https://developer.twitter.com/en/portal/dashboard](https://developer.twitter.com/en/portal/dashboard)
2. Create a new **Project & App**.
3. Copy the **Bearer Token** from the Keys & Tokens section.
4. Create a `.env` file in the root folder:

# Clone the repo
git clone https://github.com/itsprincekumar1/tweets_fetcher.git
cd tweets_fetcher

# Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

## 🖥️ Usage

```bash
python main.py <username>
```
## Example
```bash
python main.py elonmusk
```
## Output
```text
📢 Latest tweet from @elonmusk:

Just launched Starlink for maritime use. Boats now have WiFi at sea!
```
# Troubleshooting Guide

## 429 Too Many Requests
You're hitting the rate limit. The X API free tier allows limited requests per 15 minutes. Wait a while and try again.

## ModuleNotFoundError
Ensure all dependencies are installed using:

```bash
pip install -r requirements.txt
```
### ❌ ModuleNotFoundError: No module named 'click'
Make sure you're in the right virtual environment where click is installed. You can verify with:
```bash 
pip show click
```
If it's not found, install it manually:
```bash
pip install click
```
# 📦 Dependencies
- tweepy
- click
- python-dotenv

# 👨‍💻 Author
- Prince Kumar — https://github.com/itsprincekumar1/

# 🧱 Future Enhancements
- Add --count flag to fetch multiple tweets
- Save tweets to a .txt or .json file
- Add user profile metadata and avatar in CLI output
- Schedule background tweet fetching using cron
- Add logging and analytics

# ⚠️ Disclaimer
This project uses the free tier of the official Twitter/X API and is intended for educational and personal use only.
Please adhere to Twitter's API usage policies.

