import random
num=random.randint(1,100)
try:
    guess = int(input("I'm thinking of a number between 1 and 100, guess it:"))
    again="Y"
    #Ive made a variable 'again' and initialy gave it 'Y', and then ive checked if 'again' is equal to Y
    while again=="Y":
        if guess > num:
            guess = int(input("The number I'm thinking is smaller, Try again: "))
        elif guess < num:
            guess = int(input("The number I'm thinking is larger, Try again: "))
        else:
            again = input("Thats correct! Would you like to try again?(Y/N) : ").title()
            #If the user didn't input 'Y' then exit the loop
            if again != 'Y':
                break

            #Now after we type 'Y', we need this question input shown below to appear again
            else :
                guess = int(input("I'm thinking of a number between 1 and 100, guess it:"))
    print("Thank you for playing.")
#When user types something other than a number
except:
    print("WHY DID YOU PUT A LETTER?! I asked for a number. Can't you read?!!")