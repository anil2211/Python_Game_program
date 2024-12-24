import random

print("Hi...!, Welcome the the Game.\nThis is the Number Guessing Game.\nYou got only 7 chances to guess the number.Let's  start the Game")

number_to_guess=random.randrange(100)
print(number_to_guess)
chances=7

guess_counter=0

while guess_counter<chances:
    guess_counter=guess_counter+1
    my_guess=int(input("Please enter your Guess Number (range:1-100):"))

    if my_guess==number_to_guess:
        if guess_counter<=3:
            print(f"Congrtulations......\nThe number is {number_to_guess} and you found it right!! in the {guess_counter} attempt")
            break
        else:
            print(f"The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt")

    elif guess_counter>=chances and my_guess != number_to_guess:
        print(f"Oops sorry,The number is {number_to_guess} better luck next time")
    elif my_guess>number_to_guess:
        print("Your guess number is High")
    elif my_guess<number_to_guess:
        print("Your guess is Less") 
