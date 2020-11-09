
class Room:

    """This is a class that defines and area in the game."""
    def __init__(self, description, north, south, east, west, up, down):

        """Assigning the variables to the attributes."""
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down


class Item:
    """Defines an Item class."""
    def __init__(self, room_number, long_description, short_name, picked_up):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name
        self.picked_up = picked_up


def main():
    """This is the main function that all actions fall under"""
    # Creating a list to store rooms
    room_list = []
    """Creating all of the rooms."""
    room = Room("You are in what looks like the mudroom of the house."
                "\nThere is a door cracked open to the west that seems to be a bathroom."
                "\nThere is an opening north of you to the foyer.", 3, None, None, 1, None, None)
    room_list.append(room)

    room = Room("You are now in a disgusting bathroom. \nIt seems the toilet is clogged."
                "\nThere are spiders keeping you company."
                "\nThe only way out is to go back through the door to the west.", None, None, None, 0, None, None)
    room_list.append(room)

    room = Room("You are in what looks to be a dining room."
                "\nIt is very dusty and doesn't look like anyone has eaten here in a while."
                "\nThere is the kitchen to the north and the foyer to the east.", 5, None, 3, None, None, None)
    room_list.append(room)

    room = Room("You stand in the main foyer with a grand staircase in the middle of the room."
                "\nNorth or up, leads upstairs. South leads you to the mudroom."
                "\nEast leads to the office and west is the dining room.", 9, 0, 4, 3, 9, None)
    room_list.append(room)

    room = Room("You see two large sofa chairs that seem like they've seen better days in this office."
                "\nTo the west is the foyer"
                "\n*Behind the bookcase is stairway to the basement.", None, None, 13, 3, None, 13)
    room_list.append(room)

    room = Room("Standing in this very bloody and gross kitchen you wonder if anyone lives here."
                "\nTo the north is a large door that looks like a walk-in freezer."
                "\nTo the south is the dining room. East is the living room.", 6, 2, 7, None, None, None)
    room_list.append(room)

    room = Room("You see bodies swinging gently back and forth. You're standing in a freezer."
                "\nThe only exit is south back into the kitchen.", None, 5, None, None, None, None)
    room_list.append(room)

    room = Room("You stand in the living room with the TV buzzing with black and white fuzz."
                "\n It seems this place is real dusty."
                "\n To the west is the kitchen and the east is a closet door.", None, None, 8, 5, None, None)
    room_list.append(room)

    room = Room("You're in these dusty old people clothes. You must be hard to spot from outside while in the closet."
                "\n The only exit is back to the living room, west.", None, None, None, 7, None, None)
    room_list.append(room)

    room = Room("You stand at the top of the stairs. You can see how big the house really is from up here."
                "\nTo the north is a closet door. To the south is a ")
    item_list = []
    item = Item()
    item_list.append(item)

    current_room = 0
    done = False


if __name__ == "__main__":
    main()

