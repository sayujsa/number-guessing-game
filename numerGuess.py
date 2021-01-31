import random
num=random.randint(1,100)
try:
    guess = int(input("I'm thinking of a number between 1 and 100, guess it: "))
    while num != guess:
        if guess > num:
            guess = int(input("The number I'm thinking is smaller, Try again : "))
        else:
            guess = int(input("The number I'm thinking is larger, Try again : "))
    again = input("Thats correct! Would you like to try again?(Y/N) : ")
    while again.lower() != "y" and again.lower() != "n":
        again = input("Please enter (Y) or (N). Would you like to play again? : ")
    if again.lower() == "y":
        num = random.randint(1, 100)
        guess = int(input("I'm thinking of a number between 1 and 100, guess it: "))
        while num != guess:
            if guess > num:
                guess = int(input("The number I'm thinking is smaller, Try again : "))
            else:
                guess = int(input("The number I'm thinking is larger, Try again : "))
        print("Thats correct!")
    elif again.lower() == "n":
        print("Thank you for playing.")
except:
    print("You've broke the game! Dammit!")