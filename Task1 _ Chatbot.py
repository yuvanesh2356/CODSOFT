print("====================================")
print("      SMART AI CHATBOT")
print("====================================")

print("Type 'bye' to stop the chatbot.\n")

while True:

    user_input = input("You : ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Zyra: Hi, I am Zyra. Nice to chat with you.")

    elif "your name" in user_input:
        print("Zyra: My name is Zyra. I am a simple AI chatbot created using Python.")

    elif "how are you" in user_input:
        print("Zyra: I am doing well. Thanks for asking!")

    elif "ai" in user_input:
        print("Zyra: AI stands for Artificial Intelligence. It helps machines think and learn like humans.")
        
    elif "python" in user_input:
        print("Zyra: Python is a simple and powerful programming language used in AI, web development, and data science.")

    elif "time" in user_input:
        from datetime import datetime

        current_time = datetime.now().strftime("%I:%M %p")

        print("Zyra: Current time is", current_time)

    elif "date" in user_input:
        from datetime import date

        today = date.today()

        print("Zyra: Today's date is", today)

    elif "help" in user_input:
        print("Zyra: You can ask me about AI, Python, time, or date.")

    elif "joke" in user_input:
        print("Zyra: Why did the computer go to sleep? Because it was tired!")

    elif user_input == "bye":
        print("Zyra: Goodbye! Have a great day.")
        break

    else:
        print("Zyra: Sorry, I didn't understand that.")
