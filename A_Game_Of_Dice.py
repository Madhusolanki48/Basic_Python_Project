"""
In this project, we will look at how you can emulate a player throwing a set of dice. Then we 
will look at how you can store these dice in a pile the player wants to keep. you write a game where 
you throw dice to determine the outcome, this is one way to store the results for later use. example, 
normal dice with six eyes. The program will work no matter how many eyes your dice have.
"""
import random
print("Welcome {name} !\nLet's play a game of Dice")
while(1):
    player1=input("Enter the name of player1=")
    player2=input("Enter the name of player1=")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(f"{player1} score:{dice1}\n{player2} score:{dice2}")
    if(dice1>dice2):
        print(f"{player1} Won")
    elif(dice2>dice1):
        print(f"{player2} Won")
    else:
        print("Draw")
    print("Do you want to play again?\nPress 1 else Press 0")
    if(int(input())==0):
        print("Game over....\nGoodBye!")
        break
