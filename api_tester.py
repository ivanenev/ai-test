import os
from dotenv import load_dotenv
import tiktoken
import requests
import speech_recognition as sr
import pyttsx3

# Load environment variables
load_dotenv()

MODEL_PROVIDERS = {
    'TOGETHER_API_KEY': 'https://api.together.xyz/v1/models',
    'AUTHOBSIDIAN': 'https://api.obsidian.md/auth',
    'DEEPGRAM_API_KEY': 'https://api.deepgram.com/v1/projects',
    'GROK2_API_KEY': 'https://api.groq.com/v1/models',
    'GITHUB_API_KEY': 'https://api.github.com/user',
    'SERPER_API_KEY': 'https://google.serper.dev/search',
    'ANTHROPIC_API_KEY': 'https://api.anthropic.com/v1/messages',
    'OPENAIAPI_KEY': 'https://api.openai.com/v1/models',
    'DEEPSEEK_API_KEY': 'https://api.deepseek.com/v1/models'
}

def test_provider(provider, api_key):
    """Test if a provider's API key works"""
    url = MODEL_PROVIDERS[provider]
    headers = {'Authorization': f'Bearer {api_key}'}
    
    try:
        if provider == 'SERPER_API_KEY':
            # Serper requires POST with query
            response = requests.post(url, json={'q': 'test'}, headers=headers)
        else:
            response = requests.get(url, headers=headers)
        
        return response.status_code == 200
    except Exception:
        return False

def analyze_providers():
    """Analyze which providers have valid API keys"""
    # Set UTF-8 encoding for Windows console
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("API Provider Analysis:")
    print("=" * 40)
    
    for provider in MODEL_PROVIDERS:
        api_key = os.getenv(provider)
        if api_key:
            status = "✓ Working" if test_provider(provider, api_key) else "✗ Invalid"
            print(f"{provider}: {status}")
        else:
            print(f"{provider}: ✗ Not found in .env")

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
    print("1. Test API Providers")
    print("2. Voice Chat with DeepSeek")
    choice = input("Choose option (1 or 2): ")
    
    if choice == '1':
        analyze_providers()
    elif choice == '2':
        chat_with_deepseek()
