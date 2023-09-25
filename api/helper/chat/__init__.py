import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def initialize_messages(message):
    """Initialize the chat messages with system and user messages."""
    return [
        {"role": "system", "content": "You're a kind helpful assistant, only respond with knowledge you know for sure, don't hallucinate information."},
        {"role": "user", "content": message},
    ]

def add_message(messages, role, content):
    """Add a message to the list of chat messages."""
    messages.append({"role": role, "content": content})

def generate_chat_response(messages):
    """Generate a chat response using the OpenAI API."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']
