import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import random

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Sample responses database
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "name": ["I'm an AI chatbot created to assist you.", "You can call me ChatBot!"],
    "age": ["I don't age like humans do, but I was created recently."],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?", "I'm not sure how to respond."]
}

# Intent detection based on keywords
def identify_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    
    if any(word in lemmas for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in lemmas for word in ["bye", "goodbye", "see you"]):
        return "goodbye"
    elif any(word in lemmas for word in ["thanks", "thank", "thankyou"]):
        return "thanks"
    elif "name" in lemmas:
        return "name"
    elif "age" in lemmas:
        return "age"
    else:
        return "default"

# Chat loop
def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("🤖 ChatBot:", random.choice(responses["goodbye"]))
            break
        intent = identify_intent(user_input)
        print("🤖 ChatBot:", random.choice(responses[intent]))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
