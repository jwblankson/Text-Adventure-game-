#Welcome to my text  adventure game!
import time
import random
import sys
import os

import pyfiglet




# Initialize player statistics and backpack
backpack = []
player_statistics = {
    "health": 10,
    "wealth": 0,
    "treasures_found" : 0
}
# Save game
def save_game(statistics, backpack):
    with open("savegame.txt", "w") as file:
        file.write(f"{statistics}\n")
        file.write(f"{backpack}\n")
    print("Game saved successfully.")  

 # Load game
def load_game():
    if os.path.exists("savegame.txt"):
        with open("savegame.txt", "r") as file:
            lines = file.readlines()
            player_statistics = eval(lines[0].strip())
            backpack = eval(lines[1].strip())
        print("Game loaded successfully.")
        return player_statistics, backpack
    else:
        print("No saved game found.")
        return None, None    

 #Function to display player statistics   
def show_player_statistics(): 
    print("please wait whiles we show your statistics... ")
    time.sleep(3)

    for key, value in player_statistics.items():
        print(f"{key}: {value}")

# Check health status
def check_health():
    if player_statistics["health"] <= 0:
        print("Your health has dropped to zero. Game over!")
        sys.exit() 




# Function to check backpack items
def check_backpack():
    if backpack:
        print("You have the following items in your backpack:")
        for items in backpack:
            print(f"- {items}")
    else:
        print("Your backpack is empty.")
# Haunted room 
def haunted_room(statistics, backpack):
    while True:
        os.system('clear')
        check_health()
        # Haunted room 
        print("\n\nYou are in a haunted room.")
        print("type 'save game' to save you progress\n\n")
        print("There is a ghost here!")
        print("There is a door to the right.")
        print("To fight the ghost, type 'fight'. (to fight the ghost you are going to loose 10 health)")
        print("To run away from the ghost, type 'run'. (to run away you are going to loose 5 health)")
        print("To go through the door, type 'go right'.(if you go right you are going to loose 5 health)")
        print("enter 'stats' to view your player statistcics or 'backpack' items in your backpack.")

    
        print("Type exit to exit the game\n")
        
        # Get user input
        choice = input(">").lower()
        if choice == "fight":
            statistics["health"] -= 20
            print("You fought the ghost and won!")
            time.sleep(2)
        elif choice == "save game":
            save_game(statistics, backpack)
            time.sleep(2)
        elif choice == "run":
            statistics["health"] -= 5
            print("You ran away from the ghost.")
            time.sleep(2)    
        elif choice == "go right":
            statistics["health"] -= 5      
            print("You go through the door and find yourself in an office space.")
            time.sleep(2)
            print("You find a treasure chest would you want to open it? (yes or no)")
            pick = input(">").lower()
            if pick == "yes":
                print("You opened the treasure chest and found 100 gold coins!")
                statistics["wealth"] += 100
                statistics["treasures_found"] += 1
                time.sleep(2)
        elif choice == "exit":
            print("Exiting the game. Goodbye!")
            break
            
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
            sys.exit()
        else:
            print(" Please type a valid command")
            time.sleep(2)   
    return statistics, backpack 

#Office space
def office_space(statistics, backpack):
    
    
    while True:
        os.system('clear')
        check_health()
        # Office space scenario
        print("\n\nYou are in the office space.")
        print("There is a desk with a computer.")
        print("There is a door to the left.")
        print("To use the computer, type 'use computer'.(to use the computer you are going to loose 10 health)")
        print("To go through the door, type 'go left'.")
        print("enter 'stats' to view your player statistcics or 'backpack' items in your backpack.")



        print("Type exit to exit the game\n")
        
        # Get user input
        choice = input(">").lower()
        if choice == "use computer":
            statistics["health"] -= 10
            print("You use the computer and find a secret message.")
            time.sleep(2)
        elif choice == "go left":      
            print("You go through the door and find yourself in a hallway.")
            time.sleep(2)
            print("You find a chocolate bar on the floor would you want to pick it up? (yes or no)")
            pick = input(">").lower()
            if pick == "yes":
                print("You picked up the chocolate bar and added it to your backpack.")
                backpack.append("chocolate bar")
                time.sleep(2)
        elif choice == "exit":
            print("Exiting the game. Goodbye!")
            break
            
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
            sys.exit()
        else:
            print("Invalid choice. Please type 'use computer' or 'go left'.")
    return statistics, backpack 






rooms = ["haunted room", "office space"]
# Main game loop
while True:
    os.system('clear')
    print("****************************************************************")
    ASCII_art_1 = pyfiglet.figlet_format("TEXT ADVENTURE")
    print(ASCII_art_1)
    time.sleep(1)
    print("\n\nWelcome to the text adventure game!")
    print("to load the previous game type 'load' or type 'start' to start a new game or 'exit' to end the game.\n")
    user_input = input(">").lower()
    if user_input == "load":    
        player_statistics,backpack = load_game()
        time.sleep(2)
    elif user_input == "exit":
        print("Exiting the game. Goodbye!")
        sys.exit()
    elif user_input == "start":
        print("Starting a new game...")
        time.sleep(2)
    else:
        print("Invalid choice. Please type 'load' or 'start'.")
        continue
    time.sleep(1)
    os.system('clear')
    print("enter 'stats' to view your player statistcics or 'backpack' items in your backpack.")
    print("type 'save' to save current progress or 'end game' to exit the game.\n\n")
    print("Which room would you like to explore?(haunted room or office space)")
    for room in rooms:
        print(f"- {room}")

    


    choice = input(">").lower()

    # Handle user input
    if choice == "office space":
        print("please wait...")
        time.sleep(2)
        # Explore the office space
        office_space(player_statistics, backpack)
    

    elif choice == "haunted room":
        print("please wait...")
        time.sleep(2)
        # Explore the haunted room
        haunted_room(player_statistics, backpack)
        
    elif choice == "save":
        # Save the game
        save_game(player_statistics, backpack)
        time.sleep(2)

        
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
        print("Pleae eneter a valid command")
        time.sleep(2)



