import requests
from send_email import send_email
import datetime
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configurations
API_KEY = os.getenv("NEWS_API_KEY") 
TODAY = datetime.date.today()

def get_news(topic="business", country="us"):
    """Fetches top headlines from NewsAPI."""
    if not API_KEY:
        return None

    url = f"https://newsapi.org/v2/top-headlines?country={country}&category={topic}&apiKey={API_KEY}&language=en"
    
    try:
        response = requests.get(url)
        content = response.json()
        if content.get('status') == 'ok':
            return content['articles']
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def build_html_body(articles, topic):
    """
    Constructs a beautiful HTML email body with CSS styling and Images.
    """
    html = f"""
    <html>
      <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            
            <div style="background-color: #2c3e50; padding: 25px; text-align: center; border-radius: 5px 5px 0 0;">
                <h1 style="color: white; margin: 0; font-size: 26px;">Daily News Digest</h1>
                <p style="color: #bdc3c7; margin: 10px 0 0 0; font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">{topic.title()} Edition | {TODAY}</p>
            </div>
            
            <div style="padding: 20px;">
    """
    
    for article in articles[:10]:
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image_url = article.get('urlToImage') # Get the image URL

        if title and description and url:
            html += f"""
            <div style="margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid #eeeeee;">
            """
            
            # --- IMAGE BLOCK ---
            # We only add the image tag if a URL exists
            if image_url:
                html += f"""
                <a href="{url}" style="text-decoration: none;">
                    <img src="{image_url}" alt="News Image" style="width: 100%; max-width: 600px; height: auto; border-radius: 5px; margin-bottom: 15px; object-fit: cover;">
                </a>
                """
            # -------------------

            html += f"""
                <h3 style="margin-top: 0; margin-bottom: 10px; color: #2c3e50; font-size: 18px; line-height: 1.4;">
                    <a href="{url}" style="text-decoration: none; color: #2c3e50;">{title}</a>
                </h3>
                <p style="color: #666666; line-height: 1.6; font-size: 14px; margin-bottom: 15px;">{description}</p>
                <a href="{url}" style="display: inline-block; background-color: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-size: 13px; font-weight: bold;">Read Full Story &rarr;</a>
            </div>
            """
    
    html += """
            </div>
            <div style="text-align: center; padding: 20px; color: #999; font-size: 12px; border-top: 1px solid #eee;">
                <p>Automated with Python by Joao Costa | News provided by NewsAPI</p>
            </div>
        </div>
      </body>
    </html>
    """
    return html

# --- Execution ---

if len(sys.argv) > 1:
    topic_choice = sys.argv[1]
else:
    topic_choice = "business" 

print(f"Fetching news for topic: {topic_choice}...")
articles = get_news(topic=topic_choice)

if articles:
    # Build the HTML content
    email_content = build_html_body(articles, topic_choice)
    
    # Define the Subject line
    subject = f"📰 {topic_choice.title()} News - {TODAY}"
    
    # Send using the new function
    send_email(subject, email_content)
else:
    print("No news found or API error.")