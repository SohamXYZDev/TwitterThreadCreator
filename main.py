import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from newspaper import Article
import json
import requests

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables
url = os.getenv('CONTENT_URL', 'https://www.youtube.com/watch?v=EXAMPLE_VIDEO_ID')
webhook_url = os.getenv('DEFAULT_WEBHOOK_URL', 'http://localhost:5678/webhook-test/YOUR_WEBHOOK_ID')

# Check if it's a YouTube URL
is_youtube = "youtu.be" in url or "youtube.com" in url

if is_youtube:
    # Extract the video ID from the URL
    if "youtu.be" in url:
        video_id = url.split("/")[-1]
    elif "youtube.com/watch?v=" in url:
        video_id = url.split("v=")[-1].split("&")[0]
    elif "youtube.com/embed/" in url:
        video_id = url.split("/")[-1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL format")
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([x["text"] for x in transcript])
        
        # Prepare data to send to webhook
        data = {"transcript": text, "id": video_id}
        
        # send to webhook
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 200:
            print(json.dumps({"success": True, "message": "Transcript sent successfully"}))
        else:
            print(json.dumps({"success": False, "error": f"Failed to send transcript. Status code: {response.status_code}"}))
            
    except Exception as e:
        print(json.dumps({ "error": str(e) }))
else:
    # Not a YouTube URL, extract article content
    try:
        # Use newspaper to extract article content
        article = Article(url)
        article.download()
        article.parse()
        
        # Prepare data to send to webhook
        data = {
            "url": url,
            "title": article.title,
            "text": article.text
        }
        
        # Send to webhook
        webhook_url = os.getenv('WEBHOOK_URL_REMOTE', os.getenv('DEFAULT_WEBHOOK_URL', 'http://localhost:5678/webhook-test/YOUR_WEBHOOK_ID'))
        response = requests.post(webhook_url, json=data)
        
        if response.status_code == 200:
            print(json.dumps({"success": True, "message": "Article sent successfully"}))
        else:
            print(json.dumps({"success": False, "error": f"Failed to send article. Status code: {response.status_code}"}))
            
    except Exception as e:
        print(json.dumps({ "error": str(e) }))

