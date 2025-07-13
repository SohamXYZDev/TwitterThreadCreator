# Twitter Thread Creator

An automated system that transforms YouTube videos and web articles into engaging Twitter threads using AI. This project combines a Python script for content extraction with an n8n workflow for AI processing and automated posting to Twitter/X.

## 🚀 Features

- **Multi-Source Content Support**: Extract content from YouTube videos (via transcripts) and web articles
- **AI-Powered Thread Generation**: Uses Google Gemini or other AI models to intelligently break down content into Twitter-friendly threads
- **Automated Posting**: Automatically posts main tweets and threaded replies to Twitter/X
- **Visual Enhancement**: Supports thumbnail extraction and image posting for YouTube videos
- **Workflow Management**: Complete n8n automation workflow with error handling and retry logic
- **Google Docs Integration**: Tracks tweet IDs for thread management

## 📁 Project Structure

- `main.py` - Python script for content extraction and webhook integration
- `Twitter_Thread_Creator.json` - n8n workflow configuration for AI processing and Twitter posting
- `.env.example` - Template for environment variables configuration
- `.env` - Your personal environment configuration (create from .env.example)

## 🛠️ Installation & Setup

### Prerequisites

The following credentials and APIs are required:

- **YouTube OAuth2 API** - For video metadata extraction
- **AI Model Access** (Google Gemini, OpenAI, etc.) - For thread generation
- **Twitter/X API Credentials**:
  - OAuth 1.0 (API Key and Secret) - For image uploads
  - OAuth 2.0 (Client ID and Secret) - For posting tweets
- **Google Docs OAuth2 API** - For tweet ID tracking
- **n8n Instance** - For workflow automation

### Python Environment Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/SohamXYZDev/TwitterThreadCreator
   cd TwitterThreadCreator
   ```

2. **Install Python dependencies**:

   ```bash
   pip install youtube_transcript_api newspaper3k lxml_html_clean requests python-dotenv
   ```

3. **Configure environment variables**:

   ```bash
   # Copy the example environment file
   cp .env.example .env

   # Edit .env file with your actual values
   # Set your content URL and webhook endpoints
   ```

4. **Update your .env file**:
   ```env
   CONTENT_URL=https://www.youtube.com/watch?v=YOUR_VIDEO_ID
   DEFAULT_WEBHOOK_URL=https://your-n8n-instance.com/webhook/YOUR_WEBHOOK_ID
   WEBHOOK_URL_REMOTE=https://your-n8n-instance.com/webhook/YOUR_WEBHOOK_ID
   ```

### n8n Workflow Setup

1. **Import the workflow**:
   - Import `Twitter_Thread_Creator.json` into your n8n instance
2. **Configure credentials**:
   - Set up all required API credentials in n8n:
     - YouTube OAuth2 API (replace `YOUR_YOUTUBE_OAUTH_ID`)
     - Google Gemini API (replace `YOUR_GEMINI_API_ID`)
     - Twitter OAuth2 API (replace `YOUR_TWITTER_OAUTH_ID`)
     - Google Docs OAuth2 API (replace `YOUR_GOOGLE_DOCS_OAUTH_ID`)
3. **Configure Google Docs**:
   - Create a new Google Doc for tweet ID tracking
   - Replace `YOUR_GOOGLE_DOC_ID` in all Google Docs nodes with your document ID
   - Extract the document ID from your Google Doc URL: `https://docs.google.com/document/d/DOCUMENT_ID/edit`
4. **Configure webhook**:
   - Note the webhook URL from the imported workflow
   - Update your `.env` file with the correct webhook URL

## 🚀 Quick Start

**For first-time setup:**

1. **Get Google Doc ID**: Create a Google Doc, extract ID from URL: `https://docs.google.com/document/d/YOUR_DOC_ID/edit`
2. **Import the Workflow**: Import `Twitter_Thread_Creator.json` into n8n.
2. **Add credentials**: Add the above mentioned credentials to the workflow.
3. **Test**: Set URL in `.env` and run `python main.py`

## 🎯 Usage

### For YouTube Videos

1. Set a YouTube URL in your `.env` file:
   ```env
   CONTENT_URL=https://www.youtube.com/watch?v=YOUR_VIDEO_ID
   ```
2. Run the Python script:
   ```bash
   python main.py
   ```
3. The workflow will:
   - Extract video transcript and metadata
   - Generate AI-powered Twitter thread
   - Post main tweet with video thumbnail
   - Post threaded replies automatically

### For Web Articles

1. Set any article URL in your `.env` file:
   ```env
   CONTENT_URL=https://example.com/your-article
   ```
2. Run the script - it will automatically detect non-YouTube URLs
3. The workflow processes article title and content into a Twitter thread

## 📊 How It Works

### Content Extraction (Python Script)

- **YouTube Videos**: Extracts transcript using YouTube Transcript API
- **Web Articles**: Scrapes content using newspaper3k library
- **Data Format**: Sends structured JSON to n8n webhook

### AI Processing (n8n Workflow)

- **Content Analysis**: AI model analyzes transcript/article content
- **Thread Generation**: Creates main tweet + sequential replies
- **Structured Output**: Uses JSON schema for consistent formatting

### Social Media Automation

- **Image Processing**: Downloads and uploads video thumbnails
- **Sequential Posting**: Posts main tweet first, then threaded replies
- **ID Tracking**: Saves tweet IDs in Google Docs for proper threading

## 🔧 Workflow Components

The n8n workflow includes:

- **Webhook Trigger**: Receives content from Python script
- **Content Router**: Handles YouTube vs. article processing differently
- **AI Chain**: Google Gemini integration for thread generation
- **Twitter Nodes**: Automated posting with proper threading
- **Image Upload**: Handles thumbnail extraction and posting
- **Error Handling**: Retry logic and error management
- **ID Management**: Google Docs integration for tweet tracking

## 📋 Requirements

- **Python**: 3.9+
- **Dependencies**:
  - `youtube_transcript_api` - YouTube transcript extraction
  - `newspaper3k` - Web article scraping
  - `lxml_html_clean` - HTML parsing
  - `requests` - HTTP requests
  - `python-dotenv` - Environment variable management
- **n8n**: Latest version with LangChain nodes
- **APIs**: All mentioned credentials properly configured

## 🤖 AI Model Configuration

The system supports multiple AI providers:

- **Google Gemini** (default): Fast and cost-effective
- **OpenAI GPT**: High-quality output
- **Other LangChain-compatible models**

Configure your preferred model in the n8n workflow's AI chain node.

## 🔐 Security Notes

- **Environment Variables**: Store all sensitive URLs and IDs in the `.env` file
- **Never commit `.env`**: Add `.env` to your `.gitignore` file to prevent accidental commits
- **Use `.env.example`**: Share configuration templates without exposing actual values
- Store all API credentials securely in n8n
- Use environment variables for sensitive data
- Regularly rotate API keys
- Monitor API usage and rate limits

**Important**: The `.env` file should never be committed to version control. Always use `.env.example` as a template.

## 🎨 Customization

### Thread Format

Modify the AI prompt in the n8n workflow to change:

- Thread structure and style
- Content focus and emphasis
- Tone and voice
- Length and complexity

### Content Processing

Adjust the Python script to:

- Add new content sources
- Modify data extraction logic
- Change webhook payload structure

## 🚨 Error Handling

The system includes comprehensive error handling:

- **Python Script**: JSON error responses for debugging
- **n8n Workflow**: Retry logic for failed API calls
- **Rate Limiting**: Built-in delays between posts
- **Validation**: Content and credential validation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the repository for license details.

## Socials

Created & maintained by Soham Mitra (SohamXYZ)

- 🌐 Website: [https://sohamxyz.com](https://sohamxyz.com)
- 📧 Email: soham@sohamxyz.com
- 💬 Discord: sohamxyz
- 🧠 n8n/automation/dev inquiries welcome!

---

_Transform any content into engaging Twitter threads with the power of AI automation!_
