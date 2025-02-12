def question():
    print("Hello its chatbot, how may I help you?")
    question1=input("Enter a single word prompt:")
    if question1 == "weather":
        print("The weather today is cloudy, with a 15% chance of rain. It is the best weather to stay inside and drink hot chocolate.")
    elif question1 == "hobby":
        print("Sorry I'm a chatbot! I don't have a hobby!")
    elif question1 == "chemistry":
        print("The best part of chemistry is stoichometry!")
    elif question1 == "python":
        print("Sorry I'm a chatbot! I don't know python!")
    elif question1 == "animals":
        print("My favorite animal is an eagle!")
    elif question1 == "insects":
        print("My favorite insect is the butterfly")
    elif question1 == "color":
        print("My favorite color is red")
    elif question1 == "food":
        print("My favorite food is momo")
    else:
        print("Sorry I'm a chatbot! I don't know!")          
def botmenu():
    print("Welcome to Python Chatbot")
    while True: #infinite loop
        print("Choose an option: 1. Ask chatbot a question 2. Quit")
        choice=input("Enter your choice(1-2)")
        if choice=="1":
            question()
        elif choice=="2":
            print("Thank you for talking to the chatbot")
            break
        else:
            print("Enter valid number between 1-2")
botmenu()
