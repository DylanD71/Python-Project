print("Welcome to Treasure Island")
print("Mission is to find treasure")
choice1 = input('You\'re at a crossroad, which direction do you go in?' 
                'Type "left" or "right".\n'). lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat . '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island intact."
                        "There is a house 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("you triggered a trap door and fell. Game over")
        elif choice3 == "yellow":
            print("you found the treasure. You Win!")
        elif choice3 == "blue":
            print("you enter a room with hungry lions.Game over.") 
        else:
            print("you chose a door that doesn't exist.Game over") 
    else:
        print("You got attacked by piranhas. Game over.")   

else:
    print("you fell in a deep hole. Game Over.")                       