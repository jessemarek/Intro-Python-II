import os
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# List of commands
movement = ["n", "e", "s", "w", "north", "east", "south", "west"]


# Function to start the game
def game_start():
    # clears the screen
    os.system("clear")
    # waits for user to enter name
    global user_name
    user_name = input("Welcome, Adventurer! Please enter your name: ")
    os.system("clear")
    return user_name


# Function to parse user inputs
def parse_input():
    # Takes user input and splits into list of commands
    command = input(
        f"{player.name}, enter a command: ").strip().lower().split()[0]

    # Checks commands entered and performs actions if valid
    # If the user enters a direction, attempt to move to the room there.

    # Move in direction entered
    if command in movement:
        os.system("clear")
        player.move(command)

    # If the user enters "q", quit the game.
    elif command == "q" or "quit":
        quit_game()

    # If no recognized command is entered tell the user it was not recognized
    else:
        os.system("clear")
        print("I don't understand. Please enter a valid command!")


# Function to print the game to screen
# Clears screen before printing each time
# prints results of actions determined from user input
""" def print_screen(message):
    os.system("clear")
    print(message) """


# Function to handle exiting the program
# Clear the screen
# Send goodbye message
# Exit program with no errors
def quit_game():
    os.system("clear")
    print("Goodbye, play again soon!")
    exit(0)


#
# Main
#
game_start()
# Make a new player object that is currently in the 'outside' room.
player = Player(user_name, room["outside"])

# Write a loop that:
while True:

    # * Prints the current room name
    # * Prints the current description
    print(player.location)

    # Run the command parser to decide what action to take
    parse_input()
