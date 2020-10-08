class Room:
    """This is a class that defines a room"""
    def __init__(self, description, north, south, east, west):
        """This creates the values and stores them with the room class."""
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    """This is the main function all actions fall under."""
    room_list = []
    """This is creating an empty list for our rooms to fall under."""

    """Creating the main foyer as the entrance to house"""
    room = Room("This is the main foyer. There is a locked door to the south."
                "\nThere is a laundry room to the west."
                "\nStairs to the east and the main hallway is to the north", 2, None, 3, 1)
    room_list.append(room)

    """Creating the laundry room"""
    room = Room("This is the laundry room just a bunch of clothes with a washer and dryer."
                "\nThe main foyer is to the east.", None, None, 0, None)
    room_list.append(room)

    """Creating the main hallway"""
    room = Room("This is the main hall, there's a pretty picture you admire on the wall."
                "\nThere is the foyer to the south."
                "\nThe office to the east."
                "\nThe kitchen to the north.", 8, 0, 4, None)
    room_list.append(room)

    """Creating the staircase to upstairs"""
    room = Room("You're in the staircase."
                "\nNorth is the attic."
                "\nWest is the main foyer.", 5, None, None, 0)
    room_list.append(room)

    """Creating the office"""
    room = Room("You're in the office."
                " There is one real messy desk with papers all over and three walls with big windows."
                "\nTo the west is the main hall."
                "\nThere are no other doors but the hallway.", None, None, None, 2)
    room_list.append(room)

    """Creating a spooky attic."""
    room = Room("You're in a real dusty attic, real spooky."
                "\nYou can look outside over the property and admire the well cut grass."
                "\nThe only exit is the staircase to the south.", None, 3, None, None)
    room_list.append(room)

    """Creating a weird master bedroom"""
    room = Room("You're in the master bedroom."
                "\nThere isn't much in here except a bed that goes from wall to wall."
                "\nYou really wonder why they need such a big bed."
                "\nThe only exit is east back to the hallway.", None, None, 10, None)
    room_list.append(room)

    """Creating the deck without any way down."""
    room = Room("You're standing on the deck with no stairs down."
                "\nOnly the door to the south is a exit."
                "\nAlso you wonder how bad of a fire hazard this house is.", None, 9, None, None)
    room_list.append(room)

    """Creating a kitchen."""
    room = Room("You stand in the kitchen. Man you're a little hungry, but no time now."
                "\nTo the west is the living room."
                "\nTo the south goes back into the main hallway.", None, 2, None, 9)
    room_list.append(room)

    """Creating the living room."""
    room = Room("You're in the living room. The TV is playing something stupid."
                "\nTo the north is the deck.\nTo east is the kitchen."
                "\nTo the west is a hallway.", 7, None, 8, 10)
    room_list.append(room)

    room = Room("You stand is an extremely generic hallway."
                "\nLike real generic.\nTo the north is the bathroom."
                "\nTo the west is the master bedroom.\nTo the south is the bedroom."
                "\nTo the east is the living room.", 11, 12, 9, 6)
    room_list.append(room)

    room = Room("You stand in the bathroom.\nThis is kinda weird that you're in the bathroom."
                "\nTo the south is the hallway.", None, 10, None, None)
    room_list.append(room)

    room = Room("You stand in a kid's bedroom.\nOr at least you hope, as there are toys everywhere."
                "\nTo the north is the hallway, there isn't another exit.", 10, None, None, None)
    room_list.append(room)

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
        elif direction_traveled.upper() == "Q" or direction_traveled.upper() == "QUIT":
            print("Thanks for playing!")
            done = True
        else:
            print()
            print("I don't understand that.")


if __name__ == "__main__":
    main()
