# Write a class to hold player information, e.g. what room they are in
# currently.

# Player has a name and and current room
# Player needs a way to move
# Player will need an inventory of items they can carry

class Player:
    def __init__(self, name, location, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory

    # moves player to a new room
    def move(self, direction):
        # take the direction from user input and create an attr to check
        attr = direction[0] + "_to"

        # recieves a direction to check if move is possible
        if hasattr(self.location, attr):
            self.location = getattr(self.location, attr)

        # Print an error message if the movement isn't allowed.
        else:
            print("You cannot pass that direction!")
