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


# Function to parse user inputs
# Takes user input and splits into list of commands
# Checks commands entered and performs actions if valid
# If the user enters a cardinal direction,
# attempt to move to the room there.
# Print an error message if the movement isn't allowed.
def parse_input(user_input):
    commands = user_input.split(" ")

    # Move North
    if commands[0] == "n":
        os.system("clear")
        player.move("n_to")

    # Move East
    elif commands[0] == "e":
        os.system("clear")
        player.move("e_to")

    # Move South
    elif commands[0] == "s":
        os.system("clear")
        player.move("s_to")

    # Move West
    elif commands[0] == "w":
        os.system("clear")
        player.move("w_to")

    # If the user enters "q", quit the game.
    elif commands[0] == "q":
        quit_game()

    # If no recognized command is entered tell the user it was not recognized
    else:
        os.system("clear")
        print("\nI don't understand. Please enter a valid command!\n")


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
os.system("clear")
user_name = input("Welcome, Adventurer! Please enter your name: ")
os.system("clear")
# Make a new player object that is currently in the 'outside' room.
player = Player(user_name, room["outside"])

# Write a loop that:
while True:

    # * Prints the current room name
    # * Prints the current description
    # (the textwrap module might be useful here).
    print(f"\n=== {player.current_room.name} ===\n \
    \n{player.current_room.description}\n")

    # * Waits for user input and decides what to do.
    user_input = input(f"{player.name}, enter a command: ")

    # Run the command parser to decide what action to take
    parse_input(user_input)
