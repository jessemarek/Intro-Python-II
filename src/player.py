# Write a class to hold player information, e.g. what room they are in
# currently.

# Player has a name and and location
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

        # Print an error message if the attribute doesn't exist
        # movement isn't allowed.
        else:
            raise AttributeError

    # picks up items
    def get(self, item):
        # check if item is in the location
        for i in self.location.items:
            if item == i.name.lower():
                # if the item is found pick it up
                self.inventory.append(i)
                self.location.items.remove(i)
                return f"*** You picked up the {i.name} ***"

        # if the item isn't found prints an error message
        else:
            return f"*** There is no {item} here to pick up! ***"

    # drop items from inventory
    def drop(self, item):
        # check if item is in player inventory
        for i in self.inventory:
            if item == i.name.lower():
                # if the item is found drop it in current room
                self.location.items.append(i)
                self.inventory.remove(i)
                return f"*** You dropped the {i.name} ***"

        # if the item isn't in player inventory prints an error message
        else:
            return f"*** There is no {item} in your inventory! ***"

    # looks for items in a room
    def look(self):
        # checks if room has any items
        if len(self.location.items) > 0:
            items = []
            # if the room has items prints a list of them
            for i in self.location.items:
                items.append(i.name)

            return f"*** The {self.location.name} contains {items} ***"

        # if there are no items prints `nothing interesting here`
        else:
            return "*** Nothing interesting here. ***"

    # prints list of all items in player's inventory
    def check_inv(self):
        items = []

        if len(self.inventory) > 0:
            for i in self.inventory:
                items.append(i.name)

        return f"*** Inventory: {items} ***"
