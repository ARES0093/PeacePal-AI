import streamlit as st
import requests
import os
from dotenv import load_dotenv

# For voice input
import streamlit.components.v1 as components
import tempfile
import speech_recognition as sr
from pydub import AudioSegment

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq constants
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# Function to get response from Groq
def query_groq(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": 500
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}"

# Function to recognize audio
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "API unavailable."

# Initialize session state for memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and cautious medical advisor. You provide safe, general health advice and always recommend seeing a doctor for serious issues."}
    ]

# Streamlit UI
st.set_page_config(page_title="🩺 AI Mental Chatbot", page_icon="🧠", layout="wide")
st.title("🧠 AI Mental Suggestion Chatbot ")

# Audio input section
audio_file = st.file_uploader("Upload your voice (WAV format)", type=["wav"])
if audio_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_file.read())
        temp_audio_path = temp_audio.name
    transcribed_text = transcribe_audio(temp_audio_path)
    st.text_area("🎤 Transcribed Text", value=transcribed_text, height=100)
    if st.button("Send Voice Message"):
        st.session_state.messages.append({"role": "user", "content": transcribed_text})
        response = query_groq(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Text input section
with st.form("text_chat_form", clear_on_submit=True):
    user_text = st.text_input("💬 Type your question:")
    submitted = st.form_submit_button("Send")
    if submitted and user_text:
        st.session_state.messages.append({"role": "user", "content": user_text})
        response = query_groq(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
st.markdown("## 🗣️ Chat History")
for msg in st.session_state.messages[1:]:  # Skip system message
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")