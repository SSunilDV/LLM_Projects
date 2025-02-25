import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled, NoTranscriptFound

#loaing the API key from the .env file
load_dotenv()

#setting the API key 
Api_key = os.getenv('API_KEY')
genai.configure(api_key=Api_key)

#setting the title and description of the app
st.title("Youtube Notes Generator")
st.write("This app generates notes from youtube video using Google's AI.")

#taking the input from the user and then getting the transcript text from the youtube video
url = st.text_input("Enter the youtube video link")
vid = url.split("=")[-1]

#Checking if the video transcript is present or not
if vid:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(vid)
        text = " ".join([line['text'] for line in transcript])
    except (TranscriptsDisabled, NoTranscriptFound):
        st.error("No transcript available for this video.")
        #st.stop()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        #st.stop()


prompt1 = ("As an expert, your task is to provide detailed notes based on the transcript "
               "of a YouTube video I'll provide. Assume the role of a student and generate "
               "comprehensive notes covering the key concepts discussed in the video. "
               "Also, list the tools mentioned, specifying whether they are free or paid.\n\nTranscript:")
    
prompt2 = ("As an expert, your task is to provide info based on the transcript of a YouTube video "
               "and a query I'll provide. Assume the role of a student and generate info of the video in an appropriate format "
               "based on the given query. Also, list the tools mentioned, specifying whether they are free or paid.\n\nQuery: ")

#taking the additional query from the user
query=st.text_input("Additional query on notes generation(optional)")

#generating the notes
if st.button("Generate Notes"):
    try:
        model = genai.GenerativeModel("gemini-pro")
        full_prompt = prompt2 + query + "\n\nTranscript:" + text if query else prompt1 + text
        response = model.generate_content(full_prompt)
            
        st.image(f"http://img.youtube.com/vi/{vid}/0.jpg", use_container_width=True)
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
