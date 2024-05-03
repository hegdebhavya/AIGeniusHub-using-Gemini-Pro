# YouScript: YouTube Video Summary App

This application uses Google's Generative AI to summarize the content of YouTube videos based on their transcripts. It's designed to help users quickly understand the main points of a video without watching it.

## Features

- **YouTube Video Link Input**: Users can input a YouTube video link to get a summary.
- **Transcript Extraction**: Extracts the transcript of the video using the `youtube_transcript_api`.
- **Content Summarization**: Uses Google's Generative AI to summarize the transcript, providing a concise summary in bullet points.
- **Video Thumbnail Display**: Displays the video thumbnail for a visual reference.


## Installation

1. Clone the repository.
2. Install the required packages using pip:
   
   ```
   pip install streamlit google.generativeai youtube_transcript_api dotenv
   ```
4. Set up your Google API Key in a `.env` file:
   
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

1. Run the application:
   
   ```
   streamlit run app.py
   ```
3. Open the provided URL in your web browser.
4. Input a YouTube video link in the input field and click "Get Summary".
5. The application will display the video thumbnail and a summary of the video content.

