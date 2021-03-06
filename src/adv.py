from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


stone = Item("stone", "healing")
sword = Item("sword", "fight off enemies")
pan = Item("pan", "cooking hearty meals")

room['foyer'].item.append(stone)
room['treasure'].item.append(sword)
room['narrow'].item.append(pan)

# print(room['outside'].n_to)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(input("What is your name? "), room['outside'], None)

print(f"Hello, {player.name}.\n\n{player.current_room}")

#Maybe do not need:
# player_item = player.item

# current_room_item = player.current_room.item
# print('Your LifeSavers: ', player.item)
# Write a loop that:
#

# playerInput = ''
# while playerInput != 'Q':
#     print(
#         'Choose your next move: [N] North [S] South [E] East [W] West [Q] Quit')
#     playerInput = input(">>").upper()


while True:
    print(player.current_room)
    cmd = input("=>").lower()
    if cmd in ["n", "s", "e", "w"]:
        #Move to that room
        if cmd == "n":
            if player.current_room.n_to is not None:
                player.current_room = player.current_room.n_to
            else: 
                print("You hit a wall!")
        if cmd == "s":
            if player.current_room.s_to is not None:
                player.current_room = player.current_room.s_to
            else: 
                print("You hit a wall!")
        if cmd == "e":
            if player.current_room.e_to is not None:
                player.current_room = player.current_room.e_to
            else: 
                print("You hit a wall!")
        if cmd == "w":
            if player.current_room.w_to is not None:
                player.current_room = player.current_room.w_to
            else: 
                print("You hit a wall!")
        #     else:
        # print("I did not understand that command?")
    elif cmd == "q":
        exit()
    # elif cur_room == 'GET':
    #     player.inventory.append(item)
    #     print(f'You just picked up a {item}')

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
