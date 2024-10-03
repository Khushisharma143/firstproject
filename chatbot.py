 responses = {
    'hello': ['Hi!', 'Hello!', 'Hey!'],
    'how are you': ['I am good, thanks!', 'I am fine, thanks!', 'I am great, thanks!'],
    'what is your name': ['My name is ChatBot!', 'I am ChatBot!', 'You can call me ChatBot!'],
    'exit': ['Goodbye!', 'See you later!', 'Have a nice day!']
}

def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    # Check if user input is in the responses dictionary
    if user_input in responses:
        # Return a random response from the list of responses
        return responses.choice(responses[user_input])
    else:
        # Return a default response if user input is not in the dictionary
        return 'I did not understand that.'

def main():
    print('Welcome to the chatbot!')
    while True:
        user_input = input('please enter your message: ')