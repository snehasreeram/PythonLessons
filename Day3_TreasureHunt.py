print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

game_on = True
while game_on:

    choice1 = input("Do you choose to go Left or Right?\n").lower()

    if choice1 == "left":
        print("You've come to a lake. There is an island in the middle of the lake.")
        choice2 = input("Do you choose to Swim or Wait?\n").lower()
        if choice2 == "wait":
            print("You arrive at the island unharmed. There is a house with 3 doors.")
            choice3 = input("Which door do you choose: Red, Blue or Yellow?\n").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game Over.")
                game_on = False
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
                game_on = False
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
                game_on = False
        elif choice2 == "swim":
            print("You get attacked by an angry trout. Game Over.")
            game_on = False
    else:
        print("You fell into a hole. Game Over.")
        game_on = False









