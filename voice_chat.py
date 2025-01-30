import os
from dotenv import load_dotenv
import requests
import speech_recognition as sr
import pyttsx3

# Load environment variables
load_dotenv()

def voice_to_text():
    """Convert speech to text using microphone"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that")
            return None

def text_to_voice(text):
    """Convert text to speech"""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chat_with_deepseek():
    """Voice-based chat with DeepSeek"""
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        print("DeepSeek API key not found in .env")
        return
        
    while True:
        # Get user input via voice
        user_input = voice_to_text()
        if not user_input or user_input.lower() in ['exit', 'quit']:
            break
            
        # Send to DeepSeek
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'messages': [{'role': 'user', 'content': user_input}]
        }
        
        try:
            response = requests.post(
                'https://api.deepseek.com/v1/chat/completions',
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                reply = response.json()['choices'][0]['message']['content']
                print(f"DeepSeek: {reply}")
                text_to_voice(reply)
            else:
                print(f"Error: {response.status_code}")
                text_to_voice("Sorry, there was an error")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            text_to_voice("Sorry, something went wrong")

if __name__ == "__main__":
    # First install required packages:
    # pip install SpeechRecognition pyttsx3 pyaudio
    chat_with_deepseek()
