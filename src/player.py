# Write a class to hold player information, e.g. what room they are in
# currently.

# Player has a name and and current room
# Player needs a way to move
# Player will need a list of items they can carry

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    # moves player to a new room
    def move(self, new_room):
        self.current_room = new_room
