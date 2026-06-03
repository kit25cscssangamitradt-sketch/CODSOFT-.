print("AI Friend Chatbot")
print("Type 'bye' to exit.\n")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot : Hi friend!")
    elif user == "how are you":
        print("Bot : I am doing great!. ")
    elif user ==  "your name":
        print("Bot : My name is AI Friend.")
    elif user == "tell me a joke":
        print("Bot : Why did the computer go to the doctor? Because it had a virus. ")
    elif user == "motivate me":
        print("Bot : Success comes from consistent effort. Keep going! ")
    elif user == "favorite color":
        print("Bot : I like blue because it reminds me of technology. ")
    elif user == "bye":
        print("Bot : Goodbye! Have a wonderful day! ")
        break
    else:
        print("Bot : Sorry , I don't know that yet." )         