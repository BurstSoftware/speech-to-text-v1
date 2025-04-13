import streamlit as st
import speech_recognition as sr
import pyaudio
import time

# Initialize the recognizer
r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        st.write("Adjusting for ambient noise... Please wait")
        r.adjust_for_ambient_noise(source, duration=2)
        st.write("Listening... Speak now!")
        audio = r.listen(source, timeout=None)
    return audio

def speech_to_text(audio):
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Could not request results; {str(e)}"

def main():
    st.title("Voice to Text Converter")
    st.write("Click the button below and start speaking!")
    if 'text' not in st.session_state:
        st.session_state.text = ""
    if st.button("Start Recording"):
        with st.spinner("Recording..."):
            audio = record_audio()
            text = speech_to_text(audio)
            st.session_state.text = text
    if st.session_state.text:
        st.subheader("Transcribed Text:")
        st.write(st.session_state.text)
    if st.button("Clear"):
        st.session_state.text = ""
    st.markdown("""
    ### Instructions:
    1. Click 'Start Recording' and wait for the "Listening..." message
    2. Speak clearly into your microphone
    3. The transcription will appear automatically
    4. Click 'Clear' to start over
    """)

if __name__ == "__main__":
    main()
