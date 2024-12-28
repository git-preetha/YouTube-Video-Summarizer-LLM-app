# YouTube Video Summarizer LLM app

A powerful app that generates concise and accurate summaries for YouTube videos using **Google Gemini Pro**, the latest Large Language Model (LLM). This application helps users save time by providing key insights from lengthy video content.

## Features

- 🎥 **YouTube Video Analysis**: Fetches video transcript automatically using YouTube Transcript API.
- 🖼️ **Thumbnail Extraction**: Extracts and displays the video thumbnail when the YouTube link is provided.
- 🤖 **AI-Powered Summaries**: Generates detailed summaries with the help of Google Gemini LLM.
- ⏳ **Time-Saving**: Quickly extracts key points and main ideas from any video.
- 🛠️ **Customizable Outputs**: Choose summary length or focus on specific topics.
  

## How It Works

1. **Input**: Provide the YouTube video URL.
2. **Thumbnail Display**: The app extracts and displays the video thumbnail instantly.
3. **Transcript Extraction**: The app retrieves the transcript using the YouTube Transcript API.
4. **Summarization**: Google Gemini processes the transcript and creates a concise summary.
5. **Output**: The app displays the summary.

### Prerequisites
- Python 3.10+
- API key for [Google Gemini](https://aistudio.google.com/)

### Create a virtual environment
`conda create -p venv python==3.10 -y`

### Install dependencies
`pip install -r requirements.txt`

### Configuration
- Create a .env file in the root directory and add your API key
  `GOOGLE_API_KEY=your_google_gemini_api_key`
- Save the file

### Usage
- Run the application
  `streamlit run app.py`

### Tech Stack
- Frontend: Streamlit(for the web interface)
- Backend: Python
- API:
  * Google Gemini API
  * [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) 
