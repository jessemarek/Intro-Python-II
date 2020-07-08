# Implement a class to hold room information. This should have name and
# description attributes.

# Room has a name and description
# Room will need paths to other rooms to the N, E, S and W
# Room will need to be able to store items
# Items may be either initially in the room or dropped by the player

class Room:
    def __inti__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = "none"
        self.e_to = "none"
        self.s_to = "none"
        self.w_to = "none"
