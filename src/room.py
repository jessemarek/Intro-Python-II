# Implement a class to hold room information. This should have name and
# description attributes.

# Room has a name and description
# Room will need paths to other rooms to the N, E, S and W
# Room will need to be able to contain items
# Items may be either initially in the room or dropped by the player

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"\n=== {self.name} ===\n\n{self.description}\n"
