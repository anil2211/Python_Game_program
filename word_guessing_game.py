import random
name=input("What is your Name?  ")

print("Good Luck..",name)

words=['computer','python','django','science','programming',"maths",'water','air']

words=random.choice(words)

guesses=''
turns=12

while turns>0:
    attempt=0
    for char in words:
        if char in guesses:
            print(char,end="")
        else:
            print("_")
            attempt=attempt+1
    if attempt==0:
        print("You Win")
        print("The word is: ",words)
        break
    print()
    guess=input("guess a character: ")
    guesses=guesses+guess

    if guess not in words:
        turns=turns-1
        print("Wrong")
        print("You have", + turns, "more gueses")
        

        if turns==0:
            print("You Loose")
            print("the correct ans is :",words)
