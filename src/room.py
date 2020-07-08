# Implement a class to hold room information. This should have name and
# description attributes.

# Room has a name and description
# Room will need paths to other rooms to the N, E, S and W
# Room will need to be able to contain items
# Items may be either initially in the room or dropped by the player

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
