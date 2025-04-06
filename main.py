import streamlit as st
import whisper
from gtts import gTTS
import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

def transcribe_audio(file_path):
    model = whisper.load_model("small")
    result = model.transcribe(file_path)
    return result["text"]

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text=text)
    tts.save(filename)
    return filename

def main():
    st.title("Voice-Activated Investigator")
    uploaded_audio = st.file_uploader("Upload Audio File", type=["wav", "mp3"])
    
    if uploaded_audio:
        with open("temp_audio_file", "wb") as f:
            f.write(uploaded_audio.read())
        question = transcribe_audio("temp_audio_file")
        st.write("Transcribed Question:", question)
        
        # LLM index logic
        # e.g., index = GPTSimpleVectorIndex.from_documents(SimpleDirectoryReader("cases").load_data())
        # answer = index.query(question)
        answer = f"Fake answer about your case: {question}"
        
        st.write("Answer:", answer)
        audio_file = text_to_speech(answer)
        st.audio(audio_file)

if __name__ == "__main__":
    main()
