"""
A row of dashes represents the word to guess. If the player guesses a letter in the word, the 
script writes it in all its correct positions. The player has 10 turns to guess the word. You can easily 
customize the game by changing the variables.
"""
import random
print("WELCOME TO THE HANGMAN GAME!!")
list=['pencil','monkey','secret','colour','monster','hockey','happy']
word1=random.choice(list)
guess_left=[
    
    """-------
        |    
        |
        |
        |
        |
        |
        |
    ------------""",
    """ -------
        |    |
        |    
        |
        |
        |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    
        |    
        |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    
        |   
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        -------
        |    |
        |    |
        |    O
        |    |
        |    |
        |    |
        |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|
        |    |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\ 
        |    |
        |
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\
        |    |
        |   / 
    ------------""","""
        -------
        |    |
        |    |
        |    O
        |    |
        |   /|\\
        |    |
        |   / \\
    ------------"""
    ]
while(1):
    g=0
    turns=10
    str=''
    while(turns>0):
        f=0
        for i in word1:
            if i in str:
                print(i,end=' ')
            else:
                f=1
                print("_",end=' ')
        if(f==0):
            print("YOU WON!!")
            g=1
            break
        p=input("\nGuess the letter: ")
        str=str+p
        if p not in word1:
            turns=turns-1
            print(f"Wrong Guess\nYou now have {turns} turns left to guess the right word")
        print(guess_left[10-turns])
        if(turns==0):
            print("YOU LOST")
            g=1
    if(g==1):
        print('Do you want to play play again?\nPress 1 to play again\nPress 0 to exit')
        hang=int(input())
    if(hang==0):
        print("GAME ENDS.....")
        break
