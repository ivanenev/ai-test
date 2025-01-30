import os
from dotenv import load_dotenv
import tiktoken
import requests

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

if __name__ == "__main__":
    analyze_providers()
