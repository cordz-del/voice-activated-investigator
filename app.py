import speech_recognition as sr
from gtts import gTTS
import os
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to transcribe audio to text
def transcribe_audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"

# Function to generate LLM response
def generate_llm_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to convert text to audio
def text_to_audio(text, output_file):
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)

# Main function to handle voice input and LLM response
def main():
    # Define audio file paths
    input_audio = "input.wav"
    output_audio = "output.mp3"

    # Transcribe audio to text
    text = transcribe_audio_to_text(input_audio)
    print(f"Transcribed Text: {text}")

    # Generate LLM response
    response = generate_llm_response(text)
    print(f"LLM Response: {response}")

    # Convert response text to audio
    text_to_audio(response, output_audio)
    print(f"Audio response saved to {output_audio}")

if __name__ == "__main__":
    main()
