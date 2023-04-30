"""
In this game, the computer will guess a random number and the player will try to guess what 
number it is. The game ends when the player manages to guess the number. Display the appropriate
score also. 
"""
import random
name=input("Enter Your Name: ")
print(f"WELCOME {name} TO THE GUESSING GAME")
c=1
while(c==1):
    lower=int(input("Enter the lower limit: "))
    upper=int(input("Enter the upper limit: "))
    if(upper<lower):
        print("Kindly enter a Valid Range")
    else:
        n=random.randint(lower,upper)
        print("GUESS THE NUMBER")
        number=int(input())
        c=0
        while(1):
            c=c+1
            if(n==number):
                print("Yippee!You Guessed It.")
                print("Total Number Of Guesses=",c)
                break
            else:
                if(number<n):
                    print("Try Again!")
                    print("You Guessed The Number Too Small")
                    number=int(input())
                else:
                    print("Try Again!")
                    print("You Guessed The Number Too Large")
                    number=int(input())
    print("Do you want to play again?\nIf yes, then press '1' else press '0")
    c=int(input())
print("The Game Ends here....")
