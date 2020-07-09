# Write a class to hold player information, e.g. what room they are in
# currently.

# Player has a name and and current room
# Player needs a way to move
# Player will need an inventory of items they can carry

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    # moves player to a new room
    # recieves a direction to check if move is possible
    # if move is possible do it otherwise send error message
    def move(self, direction):
        if hasattr(self.current_room, direction):
            self.current_room = getattr(self.current_room, direction)
        else:
            print("You cannot pass that direction!")
