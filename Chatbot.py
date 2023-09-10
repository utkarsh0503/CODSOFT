import random

# Define a function to get a response from the chatbot
def get_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case insensitivity
    
    # Define some predefined rules and responses
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm just a computer program, but I'm doing well!", "I don't have feelings, but thanks for asking!"],
        "Rui": ["Happy to have you here. My name is rui. I’m not a human, but I can be very helpful!"],
        "Are you a Robot?": ["No im just an chatbot"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "default": ["I'm not sure how to respond to that.", "Could you please rephrase your question?"]
    }
    
    # Check if the user input matches any predefined rules
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return random.choice(responses["default"])

# Main chat loop
print("Chatbot: Hi! My name is Rui, I'm your chatbot. You can start a conversation or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
    response = get_response(user_input)
    print("Chatbot:", response)
