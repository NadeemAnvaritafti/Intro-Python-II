# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_in_room = []

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        return_string += f"Your options: {self.get_exits()}"
        return return_string

    def get_exits(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append('s')
        if self.e_to:
            exits.append('e')
        if self.w_to:
            exits.append('w')
        return exits

    def show_items_in_room(self):
        print(f'Items available in the {self.name}:')
        if len(self.items_in_room) == 0:
            print('--Currently no items available')
        else:
            for item in self.items_in_room:
                print(item.name)
