import random
import os

class ChatBot:
    responses = {
        "greeting": ["Hello!", "Hi!", "Welcome!", "Hey, how are you?"],
        "farewell": ["Goodbye!", "See you later!", "Take care!"],
        "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
        "reply": ["I'm fine!", "Hey I'm good, thanks for asking!!", "I'm doing just well, how are you?"],
        "response": ["That's great!!", "I'm glad", "Yay"],
        "jokes": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        "default": ["I'm sorry, I didn't understand.", "Could you please rephrase?"]
    }

    def __init__(self):
        pass

    @staticmethod
    def generate_response(user_input):
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            return random.choice(ChatBot.responses["greeting"])
        elif "goodbye" in user_input or "bye" in user_input:
            return random.choice(ChatBot.responses["farewell"])
        elif "thank" in user_input:
            return random.choice(ChatBot.responses["thanks"])
        elif "are you" in user_input:
            return random.choice(ChatBot.responses["reply"])
        elif "fine" in user_input or "good" in user_input:
            return random.choice(ChatBot.responses["response"])
        elif "joke" in user_input:
            return random.choice(ChatBot.responses["jokes"])
        elif "open" in user_input:
            if "notepad" in user_input:
                os.system("notepad")
                return "Opening Notepad..."
            elif "paint" in user_input:
                os.system("mspaint")
                return "Opening Paint..."
            else:
                return "I can't open that program."
        else:
            return random.choice(ChatBot.responses["default"])

if __name__ == "__main__":
    ai = ChatBot()
    while True:
        user_input = input("User: ")
        bot_response = ai.generate_response(user_input)
        print("Bot:", bot_response)
        if "bye" in user_input:
            break



# A chatbot in AI is a computer program designed to simulate conversation with human users, especially over the internet. Here's a breakdown of how chatbots in AI work:

# 1. **Input Understanding**: When you type a message to a chatbot, it first needs to understand what you're saying. This involves natural language processing (NLP), where the chatbot analyzes the text you've entered to grasp its meaning. NLP helps the chatbot recognize keywords, phrases, and intents.

# 2. **Intent Recognition**: After understanding the input, the chatbot tries to determine what you want or what action you're asking it to perform. This is called intent recognition. For example, if you ask about the weather, the chatbot recognizes your intent as wanting to know the current weather forecast.

# 3. **Information Retrieval or Generation**: Once the chatbot knows your intent, it either retrieves information from a database or generates a response based on pre-programmed knowledge or algorithms. For instance, if you ask the chatbot for the weather, it might access a weather API to provide you with the current conditions.

# 4. **Response Generation**: Using the information it has gathered, the chatbot generates a response in natural language. This response is then presented to you in the chat interface.

# 5. **Iteration and Improvement**: Chatbots often learn from user interactions to improve their responses over time. They may use machine learning algorithms to adapt and refine their understanding of language and user preferences.

# Here are two common types:

# Rule-based Chatbots:
#     Rule-based chatbots operate on a set of predefined rules and patterns.
#     They use if-then statements or decision trees to match user input with appropriate responses.
#     Rule-based chatbots are typically used for simple and structured tasks where the conversation flow is predictable.

# AI-powered Chatbots:
#     AI-powered chatbots leverage artificial intelligence and machine learning techniques to understand and generate human-like responses.
#     They use natural language processing (NLP) and machine learning algorithms to analyze and generate responses based on user input.
#     AI chatbots are capable of understanding context, detecting sentiment, and learning from interactions to improve their performance over time.