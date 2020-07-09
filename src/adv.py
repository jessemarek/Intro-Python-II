import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item("Rock", "an ordinary rock"), ]),

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
#
# commands for movement
movement = ["n", "e", "s", "w", "north", "east", "south", "west"]

# commands for actions
actions = ["get", "drop", "look"]

# prints a list of example commands
game_help = ["h", "help", "?"]

# exits the program
exit_game = ["q", "quit"]


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
    # Reset any previous game messages
    global game_message
    game_message = ""

    # Takes user input and splits into list of commands
    user_input = input(
        f"{player.name}, enter a command: ").strip().lower().split()

    # action or command entered by player
    # assume it is the first word entered
    command = user_input[0]
    obj = None

    # object or item specific to certain actions
    # example: get sword
    # assume it is the second word entered by the user
    if len(user_input) > 1:
        obj = user_input[1]

    # Checks commands entered and performs actions if valid
    #
    # If the user enters a direction, attempt to move to the room there.
    if command in movement:
        os.system("clear")
        player.move(command)

    elif command in actions:
        os.system("clear")
        if obj:
            game_message = getattr(player, command)(obj)
        else:
            game_message = getattr(player, command)()

    # If the user enters "q" or "quit" exit the game.
    elif command in exit_game:
        quit_game()

    # If no recognized command is entered tell the user it was not recognized
    else:
        os.system("clear")
        game_message = "I don't understand. Please enter a valid command!"


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

game_message = ""

# Write a loop that:
while True:

    # * Prints the current room name
    # * Prints the current description
    print(player.location)
    print(f"{game_message}\n")

    # Run the command parser to decide what action to take
    parse_input()
