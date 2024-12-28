import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all the environment variables
import google.generativeai as genai 
import os
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are a YouTube video summariser. You will be taking the transcript text and summarising the 
entire video and providing the important summary in points within 250 words. Please provide the summary of  
the transcript text appended here: """

#extracting transcript from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=" "
        for i in transcript_text:
            transcript+=" "+i["text"]
        return transcript
    except Exception as e:
        raise e  

#Getting summary based on prompt to Google-Gemini-Pro
def generate_gemini_content(transcript_text, prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Video Summarizer") 
youtube_link=st.text_input("Paste the YouTube video link") 

if youtube_link:
    video_id=youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_container_width=True)

if st.button("Get Detailed Summary"):
    transcript_text=extract_transcript_details(youtube_link)
    if transcript_text:
        summary=generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Summary")
        st.write(summary)

