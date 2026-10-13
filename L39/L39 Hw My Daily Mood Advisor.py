
print("================================")
print("       DAILY MOOD ADVISOR")
print("================================")

name = input("What is your name? ")

print("\nHello", name + "! How are you feeling today?")
print("\nChoose your mood:")
print("1. Happy")
print("2. Sad")
print("3. Stressed")
print("4. Angry")
print("5. Tired")
print("6. Excited")

mood = input("\nEnter a number from 1 to 6: ")

if mood == "1":
    print("\nYour mood: Happy ")
    print("Advice: Enjoy your day and share your happiness!")
    print("Activity: Listen to your favourite music.")

elif mood == "2":
    print("\nYour mood: Sad ")
    print("Advice: It is okay to have difficult days.")
    print("Activity: Talk to someone you trust or do something you enjoy.")

elif mood == "3":
    print("\nYour mood: Stressed ")
    print("Advice: Take things one step at a time.")
    print("Activity: Take a short break and try some slow breathing.")

elif mood == "4":
    print("\nYour mood: Angry ")
    print("Advice: Give yourself time to calm down.")
    print("Activity: Take a break or go for a gentle walk.")

elif mood == "5":
    print("\nYour mood: Tired ")
    print("Advice: Listen to your body and take a break.")
    print("Activity: Relax, drink some water, or get enough sleep.")

elif mood == "6":
    print("\nYour mood: Excited ")
    print("Advice: Make the most of your positive energy!")
    print("Activity: Try something creative or work on a hobby.")

else:
    print("\nInvalid choice. Please run the program again")
    print("and choose a number between 1 and 6.")

print("\nThank you for using the Daily Mood Advisor!")
print("Remember: Every feeling is valid.")
