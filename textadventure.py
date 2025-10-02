#Welcome to my text  adventure game!
import time
import random
import sys
import os




# Initialize player statistics and backpack
backpack = []
player_statistics = {
    "health": 100,
    "wealth": 0,
    "treasures_found" : 0
}

 #Function to display player statistics   
def show_player_statistics():
    print("please wait whiles we show your statistics... ")
    time.sleep(3)

    for key, value in player_statistics.items():
        print(f"{key}: {value}")




# Function to check backpack items
def check_backpack():
    if backpack:
        print("You have the following items in your backpack:")
        for items in backpack:
            print(f"- {items}")
    else:
        print("Your backpack is empty.")


#Office space
def office_space():
    
    while True:
        # Office space scenario
        print("\n\nYou are in the office space.")
        print("There is a desk with a computer.")
        print("There is a door to the left.")
        print("To use the computer, type 'use computer'.")
        print("To go through the door, type 'go left'.")

        print("Type exit to exit the game\n")
        
        # Get user input
        choice = input(">").lower()
        if choice == "use computer":
            print("You use the computer and find a secret message.")
            time.sleep(2)
        elif choice == "go left":      
            print("You go through the door and find yourself in a hallway.")
            time.sleep(2)
        elif choice == "exit":
            print("Exiting the game. Goodbye!")
            break       
        elif choice == "end game":
            print("Exiting the game. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please type 'use computer' or 'go left'.")
print("Welcome to the Text Adventure Game!")

print("type 'end game' to exit the game.")



# Main game loop
while True:
    time.sleep(1)
    print("\n\nYou find yourself in a code room with an office space.")


    print("enter 'stats' to view your player statistcics or 'backpack' items in your backpack.")
    print("Would you want to explore the office space.")
    print("(yes or no)\n")
    choice = input(">").lower()

    # Handle user input
    if choice == "yes":
        # Explore the office space
        office_space()

    elif choice == "no":
        print("You decide to stay in the code room and look around.")
        
    elif choice == "stats":
        # Display player statistics
        show_player_statistics()
        time.sleep(3)
    elif choice == "backpack":
        # Check backpack items
        check_backpack()
        time.sleep(2)
    elif choice == "end game":
        print("Exiting the game. Goodbye!")
        break   

    else:
        # Handle invalid input
        print("if the user enters wrong value. Please type 'yes' or 'no'.")


