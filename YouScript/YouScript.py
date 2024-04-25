import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Styling
st.markdown("""
<style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

prompt = """You are a YouTube video summarizer. You will take the transcript text
and summarize the entire video, providing the important summary in bullet points
within 250 words. Please provide the summary of the text given here:"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id = get_video_id(youtube_video_url)
        if video_id is None:
            return None
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([item["text"] for item in transcript_list])
        return transcript
    except Exception as e:
        st.error("Failed to retrieve transcript. Please check the video link and try again.")
        return None

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

def get_video_id(url):
    """Extracts and returns video ID from a YouTube URL, or None if the URL is invalid."""
    try:
        return url.split('v=')[1].split('&')[0]
    except IndexError:
        st.error("Invalid YouTube link provided. Please ensure the link is correct.")
        return None

st.title("YouTube Video Summary")
youtube_link = st.text_input("Enter YouTube Video Link:")

if st.button("Get Summary"):
    if youtube_link:
        video_id = get_video_id(youtube_link)
        if video_id:
            thumbnail_url = f"http://img.youtube.com/vi/{video_id}/0.jpg"
            st.image(thumbnail_url, width=700, caption="Video Thumbnail")
            with st.spinner('Fetching and summarizing video content...'):
                transcript_text = extract_transcript_details(youtube_link)
                if transcript_text:
                    summary = generate_gemini_content(transcript_text, prompt)
                    st.markdown("## Detailed Notes:", unsafe_allow_html=True)
                    st.markdown(f"<div class='big-font'>{summary}</div>", unsafe_allow_html=True)
                else:
                    st.error("No transcript available for this video.")
    else:
        st.error("Please enter a YouTube video link.")
