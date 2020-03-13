# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []

    def getItem(self, item):
        return f'{item.name}: {item.description}'

    def __str__(self):
        return f"name: {self.name}\n\n description: {self.description} Room Item: {list(map(self.getItem, self.item))}"


