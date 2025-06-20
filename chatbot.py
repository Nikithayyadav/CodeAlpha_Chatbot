def chatbot():
    print("🤖 Chatbot: Hi! I'm a simple bot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi there!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm doing well, thank you!")
        elif user_input == "what's your name":
            print("🤖 Chatbot: I'm CodeBot, your friendly assistant.")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
