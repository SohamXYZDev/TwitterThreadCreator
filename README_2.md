# Twitter Thread Creator (Python Script)

A Python script that extracts content from URLs and sends it to a webhook. Supports YouTube videos (transcripts) and web articles (title + content).

## Installation

1. Clone Repo:
   ```bash
   git clone https://github.com/SohamXYZDev/TwitterThreadCreator
   ```

1. Navigate to the project directory:
   ```bash
   cd "path/to/Twitter Thread Creator"
   ```

2. Install dependencies:
   ```bash
   pip install youtube_transcript_api newspaper3k lxml_html_clean
   ```

## Usage

1. Edit `main.py` and set your URL and webhook:
   ```python
   url = "https://www.youtube.com/watch?v=VIDEO_ID"  # or any article URL
   webhook_url = "https://your-webhook-endpoint.com"
   ```

2. Run the script (Make sure your n8n workflow is listening for webhook trigger):
   ```bash
   python main.py
   ```

## Output

**YouTube Videos**: Sends `{"transcript": "...", "id": "..."}`
**Web Articles**: Sends `{"url": "...", "title": "...", "text": "..."}`

## Requirements

- Python 3.9+