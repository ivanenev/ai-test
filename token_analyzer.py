import tiktoken

def count_tokens(text):
    """Count tokens using OpenAI's tokenizer"""
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def analyze_message(message):
    """Analyze a message and print token info"""
    tokens = count_tokens(message)
    print(f"Message: {message}")
    print(f"Token count: {tokens}")
    print(f"Token breakdown:")
    
    encoding = tiktoken.get_encoding("cl100k_base")
    for token in encoding.encode(message):
        print(f"{token}: {encoding.decode_single_token_bytes(token)}")

if __name__ == "__main__":
    print("Token Analyzer")
    while True:
        message = input("\nEnter text to analyze (or 'q' to quit): ")
        if message.lower() == 'q':
            break
        analyze_message(message)
