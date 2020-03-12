from room import Room
from player import Player
from item import Item
from item import Food

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


# Add Items
rock = Item('rock', 'can be thrown as a distraction')
sandwich = Food('sandwich', 'restores health', 100)
sword = Item('sword', 'can be used to fight off enemies')
torch = Item('torch', 'can be used to illuminate areas without light')
coins = Item('coins', 'can be used to purchase items from the shop')
armor = Item('armor', 'increases your defensive attributes')
crossbow = Item('crossbow', 'can be used to fight off enemies from a distance')
potion = Item('potion', 'can be used to restore health')
shield = Item('shield', 'increases your defensive attributes')
knife = Item('knife', 'can be used to fight off enemies')


# Add Items to Rooms
room['outside'].items_in_room.append(rock)
room['foyer'].items_in_room.append(knife)
room['overlook'].items_in_room.append(torch)
room['overlook'].items_in_room.append(armor)
room['narrow'].items_in_room.append(coins)
room['narrow'].items_in_room.append(crossbow)
room['narrow'].items_in_room.append(shield)
room['treasure'].items_in_room.append(sword)
room['treasure'].items_in_room.append(potion)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Please enter your name: '), room['outside'])
print(f'Welcome {player.name}! \n')

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
valid_directions = ('n', 's', 'e', 'w')

valid_commands = {
    'n': 'move north',
    's': 'move south',
    'e': 'move east',
    'w': 'move west',
    'i': 'show inventory of items',
    'inventory': 'show inventory of items',
    'show': 'show items available in room',
    'get [item]': 'add item from room to inventory',
    'take [item]': 'add item from room to inventory',
    'drop [item]': 'remove item from inventory',
    'c': 'show valid commands',
    'q': 'quit'
}


def show_commands():
    for key, value in valid_commands.items():
        print(f'{key}: {value}')


def two_words(string):
    if len(string.split()) == 1:
        return False
    elif len(string.split()) == 2:
        return string.split()
    else:
        return 'bad command'


print('Type \'start\' to get started! \n')
print('How to play:')
show_commands()

while True:
    cmd = input('\n -->  ')

    # Direction/Passive commands
    if two_words(cmd) == False:
        if cmd == 'q':
            print('Goodbye')
            exit(0)
        elif cmd in valid_directions:
            player.move(cmd)
        elif cmd == 'i' or cmd == 'inventory':
            player.show_inventory()
        elif cmd == 'show':
            player.current_room.show_items_in_room()
        elif cmd == 'c':
            show_commands()
        elif cmd == 'start':
            print(player.current_room)
        else:
            print('I did not understand that command')

    # Improper command
    elif two_words(cmd) == 'bad command':
        print('I did not understand that command')

    # Action commands
    else:
        verb = two_words(cmd)[0]
        item_object = two_words(cmd)[1]

        if verb == 'get' or verb == 'take':
            room_item = [
                item for item in player.current_room.items_in_room if item.name == item_object]

            if len(room_item) > 0:
                player.current_room.items_in_room.remove(room_item[0])
                player.items.append(room_item[0])
                room_item[0].on_take()
            else:
                print(f'{item_object} is not available in this room')

        elif verb == 'drop':
            inventory_item = [
                item for item in player.items if item.name == item_object]

            if len(inventory_item) > 0:
                player.current_room.items_in_room.append(inventory_item[0])
                player.items.remove(inventory_item[0])
                inventory_item[0].on_drop()
            else:
                print(
                    f'You can\'t drop {item_object} because you don\'t have it in your inventory')

        else:
            print('I did not understand that command')
