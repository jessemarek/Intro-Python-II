# Items need a name and description

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"\n*** {self.name} ***\n\n{self.description}\n"
