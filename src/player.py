# Write a class to hold player information, e.g. what room they are in
# currently.

# Player has a name and and current room
# Player starts in the "outside" Room
# Player will need a list of items they can carry

class Player:
    def __init__(self, name, current_room="outside"):
        self.name = name
        self.current_room = current_room
