# AI-CHATBOT-WITH-NLP

COMPANY:CODETECH IT SOLUTIONS

NAME:ZAHED HUSSAIN

INTERN ID:CT04DZ1510

DOMAIN:PYTHON PROGRAMMING

DURATION:4 WEEKS

MENTOR:NEELA SANTOSH

DESCRIPTION:
This Python chatbot is a simple, rule-based conversational agent that uses Natural Language Processing (NLP) techniques to interpret user input and respond accordingly. It is built with the help of the Natural Language Toolkit (NLTK) library and simulates a basic human-like conversation by identifying the user's intent and giving pre-defined responses.

🧰 Tools and Libraries Used
1. nltk (Natural Language Toolkit)
Purpose: nltk is a powerful Python library for working with human language data.

Used For:

Tokenization: Breaking down user input into individual words.

Lemmatization: Reducing words to their base or dictionary form to standardize analysis.

Specific NLTK Components Used:
word_tokenize from nltk.tokenize:

Converts input text into individual word tokens.

For example, "Thanks for your help" becomes ["Thanks", "for", "your", "help"].

WordNetLemmatizer from nltk.stem:

Lemmatizes tokens to handle grammatical variations (e.g., "thanks" → "thank").

Helps improve matching accuracy for detecting intent.

2. random (Standard Python Library)
Purpose: To add variety and randomness to chatbot responses.

Used For: Selecting a random response from a predefined list using random.choice().

Core Components and Logic
1. Predefined Response Dictionary
python
Copy
Edit
responses = {
  "greeting": [...],
  "goodbye": [...],
  ...
}
This dictionary holds response categories like greetings, thanks, and farewells.

Each category maps to a list of possible responses, adding variety and a more natural feel.

2. Intent Recognition
python
Copy
Edit
def identify_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
Tokenization: Splits user input into manageable pieces.

Lemmatization: Normalizes these words to improve matching.

Example:
If the user types "Thanks a lot", the lemmatized tokens will include "thank", which the bot recognizes and responds with something from the thanks category.

3. Keyword Matching
The bot checks for certain keywords or phrases using simple if and elif statements:

python
Copy
Edit
if any(word in lemmas for word in ["hi", "hello", "hey"]):
    return "greeting"
This basic form of intent detection does not use machine learning, but it works well for limited domains.

💬 Conversation Loop
The main function, chatbot(), handles the interaction:

python
Copy
Edit
while True:
    user_input = input("🧑 You: ")
The loop continues until the user types bye, exit, or quit.

The user’s message is passed to identify_intent(), and the corresponding response is selected and printed.

📄 Final Output Example
User Interaction Example:

yaml
Copy
Edit
🤖 ChatBot: Hello! Type 'bye' to exit.
🧑 You: Hi
🤖 ChatBot: Hey!
🧑 You: What's your name?
🤖 ChatBot: I'm an AI chatbot created to assist you.
🧑 You: Thank you!
🤖 ChatBot: You're welcome!
🧑 You: Bye
🤖 ChatBot: See you later!
🎓 What You Learn From This Script
Basic NLP Techniques:

Understanding tokenization and lemmatization.

How to preprocess text for better interpretation.

Intent Recognition:

Using simple logic to determine user intent from text input.

Chatbot Logic Flow:

Building a text-based chatbot with conditional responses.

Handling exit conditions gracefully.

Use of Randomized Responses:

Makes the chatbot feel more human by avoiding repetition.

Encapsulation of Functionality:

Separating input handling, intent identification, and output response into discrete functions.

✅ Conclusion
This script demonstrates the fundamentals of creating a rule-based chatbot in Python using NLTK. It’s a great introduction to the field of NLP and conversational AI. While it lacks advanced understanding or context memory like modern AI models, it efficiently introduces concepts such as tokenization, lemmatization, intent mapping, and user interaction loops. It can serve as a stepping stone for more complex bots that use machine learning, sentiment analysis, or deep learning-based natural language understanding systems.

OUTPUT:

<img width="646" height="184" alt="Image" src="https://github.com/user-attachments/assets/fa731f56-0dc2-4414-892b-9e81bb8a200a" />



