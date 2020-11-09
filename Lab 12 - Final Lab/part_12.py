
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
    def __init__(self, room_number, long_description, short_name):
        self.room_number = room_number
        self.long_description = long_description
        self.short_name = short_name
        self.picked_up = False


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
                "\nTo the north is a closet door. To the south is a master bedroom."
                "\nTo the west looks like another bedroom and down is the foyer.", 10, 12, None, 11, None, 3)
    room_list.append(room)

    room = Room("You're in a dusty closet. There aren't a lot of clothes in here."
                "\nMight be a good hiding place. South is the  top of the stairs.", None, 9, None, None, None, None)
    room_list.append(room)

    room = Room("You stand in a dusty bedroom. There is a wall of creepy dolls and their eyes seem to follow you."
                "\nYou wonder what this room might be used for. The only exit is east to the top of the stairs.",
                None, None, 9, None, None, None)
    room_list.append(room)

    room = Room("You now stand in what looks like to be a master bedroom. It smells like death."
                "\nThere is a large impression in the mattress on one side."
                "\nIt seems the only way out the north to the top of the stairs.", 9, None, None, None, None, None)
    room_list.append(room)

    room = Room("Standing in the basement it looks like a chamber with a door to the south and north."
                "\nThere's also the stairs to the west or up that lead to the office",
                15, 14, None, 4, 4, None)
    room_list.append(room)

    room = Room("You stand in a laundry room. The room is packed with blood stained clothing."
                "\nThere is just enough space to open the door.", 13, None, None, None, None, None)
    room_list.append(room)

    room = Room("You're in a large stone hallway. You can hear water dripping."
                "\nThere are doors on the east and west walls"
                "\nThe door to the south leads to the chamber.", None, 13, 16, 17, None, None)
    room_list.append(room)

    room = Room("The room is very dark and damp. You see a large metal table in the center covered with blood."
                "\nThe chains attached to the ceiling are swaying slowly back and forth."
                "\nIt seems the only exit is back through the door, west.", None, None, None, 15, None, None)
    room_list.append(room)

    room = Room("There is a large sleeping bear in the *corner of the room. It seems to be a cave."
                "\nThere is the doorway to the east."
                "\nYou can feel a breeze coming from the tunnel to the south.", None, 18, 15, None, None, None)
    room_list.append(room)

    room = Room("It is a dark tunnel with a light at the end of it."
                "\nYou are sure you can get out if you keep going south. You can also go back north to the bear room.",
                17, 19, None, None, None, None)
    room_list.append(room)

    room = Room("You have finally escaped that creepy house.", None, None, None, None, None, None)
    room_list.append(room)

    item_list = []
    item = Item(5, "A short blunt butter knife, good for spreading jam.", "KNIFE")
    item_list.append(item)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        print()
        print("You can type q or quit to exit the game.")
        print()
        direction_traveled = str(input("Which way would you like to go? "))
        if direction_traveled.upper() == "N" or direction_traveled.upper() == "NORTH":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "S" or direction_traveled.upper() == "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "E" or direction_traveled.upper() == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "W" or direction_traveled.upper() == "WEST":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "U" or direction_traveled.upper() == "UP":
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "D" or direction_traveled.upper() == "DOWN":
            next_room = room_list[current_room].down
            if next_room is None:
                print("You cant go that way")
            else:
                current_room = next_room
        elif direction_traveled.upper() == "Q" or direction_traveled.upper() == "QUIT":
            print("Thanks for playing!")
            done = True
        else:
            print()
            print("I don't understand that.")


if __name__ == "__main__":
    main()

