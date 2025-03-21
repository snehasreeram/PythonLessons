import random as rand

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def game():
    human = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor."))
    print("You chose:")
    if human == 0 :
        print(rock)
    elif human == 1:
        print(paper)
    else:
        print(scissors)

    print("Computer chose:")
    comp = rand.randint(0,2)
    if comp == 0 :
        print(rock)
    elif comp == 1:
        print(paper)
    else:
        print(scissors)

    if human == comp:
        print("You draw.")
    elif human == 0 and comp == 2:
        print("You won.")
    elif human == 1 and comp == 0:
        print("You won.")
    elif human == 2 and comp == 1:
        print("You won.")
    else:
        print("You lost. Computer won.")

cont = True

while cont:
    game()
    play = input("What you like to play again? Y / N\n").lower()
    if play == "y":
        cont = True
    else:
        cont = False