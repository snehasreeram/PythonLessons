import random as rand
hangman_stages = [
    """
       ------
       |    |
       |    
       |    
       |    
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |    
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    --------
    GAME OVER!
    """
]


word_list = ["aardvark", "baboon", "camel"]

play_word = rand.choice(word_list)
#print(play_word)
play_word_list = list(play_word)
#print(play_word_list)

display=[]
for i in range(0,len(play_word_list)):
    display += "_"
print(display)

game_on=True

guessed = []
lives = 6
turn = 5
while game_on:

    guess = input("Enter your guess: ")
    if guess in play_word_list:
        guessed += guess
    else:
        print("Try again.")
        lives-= 1

    for j in guessed:
        for i in range(0,len(play_word_list)):
            if play_word_list[i] == j:
                display[i]=j


    print(hangman_stages[6-lives])
    print(display)

    turn -= 1
    #print(turn)
    if turn<0 or '_' not in display:
        game_on=False

        if turn>=0 and '_' not in display:
            print("You won. Good job!")
        elif turn<0:
            print("You lost.")





