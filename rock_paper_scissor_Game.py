'''
Winning Rules as follows:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins.
In this game, randint() inbuilt function is used for generating random integer values within the given range
'''

import random

print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1-Rock \n 2-Paper \n 3-Scissors \n")

    choice=int(input("Enter your choice: ")) # user choice

    while choice>3 or choice<1:
        choice=int(input("enter valid choice please(1 or 2 or 3): "))
    if choice==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    elif choice==3:
        choice_name="Scissors"

    print("User choice is : ",choice_name)
    print("Now it's Computer Turn...")

    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice_name="Rock"
    elif computer_choice==2:
        computer_choice_name="Paper"
    else :
        computer_choice_name="Scissors"

    print("Computer choice is : ",computer_choice_name)
    print(choice_name,"vs",computer_choice_name)

    if choice==computer_choice:
        result="DRAW"
    elif (choice==1 and computer_choice==2) or (computer_choice==1 and choice==2):
        result="Paper"
    elif (choice==1 and computer_choice==3) or (computer_choice==1 and choice==3):
        result="Rock"
    elif (choice==2 and computer_choice==3) or (computer_choice==2 and choice==3):
        result="Scissors"


    if result=="DRAW":
        print("It's tie")
    elif result==choice_name:
        print("User Win becoz user selected: ",choice_name)
    else:
        print("Computer Wins becoz computer selected: ",choice_name)

    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
        
print("Thanks for playing!")    

