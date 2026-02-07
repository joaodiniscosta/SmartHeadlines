# 📰 Smart Headlines

**Smart Headlines** is a Python automation tool that delivers a modern, beautifully designed daily news digest directly to your inbox. It fetches real-time headlines via NewsAPI and formats them into a responsive HTML email with images and summaries.

## 🚀 Features

- **Automated Delivery:** Runs on demand or via schedule to send news instantly.
- **Dynamic Content:** Fetches top headlines for any topic (Business, Tech, Sports, etc.).
- **Rich HTML Design:** Sends emails with CSS styling, images, and "Read More" buttons.
- **Secure:** Uses environment variables to protect API keys and email credentials.
- **Mobile Friendly:** The email layout adapts to different screen sizes.

## 🛠️ Tech Stack

- **Python 3.14.2**
- **Requests** (API fetching)
- **SMTP & SSL** (Secure email delivery)
- **Python-dotenv** (Environment variable management)
- **HTML/CSS** (Email templating)

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone [https://github.com/joaodiniscosta/smart-headlines.git](https://github.com/joaodiniscosta/smart-headlines.git)
   cd smart-headlines
   ```

2. **Create a Virtual Environment**

   ### Windows

   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

   ### Mac/Linux

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install requests python-dotenv
   ```
4. **Configuration (.env)**
   Create a file named .env in the root directory (this file is ignored by Git for security). Add your credentials:
   ```bash
   NEWS_API_KEY=your_newsapi_key_here
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_16_char_google_app_password
   EMAIL_RECEIVER=receiver_email@gmail.com
   ```

## 🏃 Usage

Run with default topic (Business):

```bash
python main.py
```

Run with a specific topic:
Pass the topic as an argument in the command line.

```bash
python main.py technology
python main.py sports
python main.py science
```

## 🤖 Automation (Optional)

You can schedule this script to run automatically every morning:

- **Windows:** Use Task Scheduler to trigger the script at 8:00 AM.
- **Mac/Linux:** Use Cron (crontab -e).
- **Cloud:** Deploy to GitHub Actions (workflow file not included by default).

## 🛡️ License

This project is open-source and available under the MIT License.

Created by Joao Dinis Costa
