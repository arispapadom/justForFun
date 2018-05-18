import random

randomNumber=random.randint(1,100)
success=False
for i in range(6):
        print("Make a guess")
        guess=int(input())
        if guess>randomNumber:
                print("Your guess is greater")
        elif guess<randomNumber:
                print("Your guess is less")
        else:
                success=True
                break

if(i<=6 and success==True):
        print("Congratulations, you win after " + str(i+1) + " tries!!")
else:
        print("Ooops you loose. The lucky number was " + str(randomNumber))

