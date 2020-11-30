"""
The Haunted Mansion
"""

import random
import arcade


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


class Enemy:
    """Defines the Enemy class."""

    def __init__(self, name, hp, attack, room_number):
        self.hp = hp
        self.attack = attack
        self.name = name
        self.room_number = room_number


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
                "\nEast leads to the office and west is the dining room.", 9, 0, 4, 2, 9, None)
    room_list.append(room)

    room = Room("You see two large sofa chairs that seem like they've seen better days in this office."
                "\nTo the west is the foyer"
                "\nIt seems to be the only exit."
                "\nThere is a bookcase on the east wall.", None, None, None, 3, None, None)
    room_list.append(room)

    room = Room("Standing in this very bloody and gross kitchen you wonder if anyone lives here."
                "\nTo the north is a large door that looks like a walk-in freezer, but it's locked."
                "\nTo the south is the dining room. East is the living room.", None, 2, 7, None, None, None)
    room_list.append(room)

    room = Room("You see bodies swinging gently back and forth. You're standing in a freezer."
                "\nThe only exit is south back into the kitchen.", None, 5, None, None, None, None)
    room_list.append(room)

    room = Room("You stand in the living room with the TV buzzing with black and white fuzz."
                "\nIt seems this place is real dusty."
                "\nTo the west is the kitchen and the east is a closet door.", None, None, 8, 5, None, None)
    room_list.append(room)

    room = Room("You're in these dusty old people clothes. You must be hard to spot from outside while in the closet."
                "\nThe only exit is back to the living room, west.", None, None, None, 7, None, None)
    room_list.append(room)

    room = Room("You stand at the top of the stairs. You can see how big the house really is from up here."
                "\nTo the north is a closet door. To the east is a master bedroom."
                "\nTo the west looks like another bedroom and south is the foyer.", 10, 3, 12, 11, None, 3)
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
                "\nIt seems the only way out the west, back to the top of the stairs.", None, None, None, 9, None, None)
    room_list.append(room)

    room = Room("Standing in the basement it looks like a chamber with a door to the south and north."
                "\nThere's also the stairs to the west or up that lead to the office",
                15, 14, None, 4, 4, None)
    room_list.append(room)

    room = Room("You stand in a laundry room. The room is packed with blood stained clothing."
                "\nThere is just enough space to open the door."
                "\nThe only way out is north to the chamber.", 13, None, None, None, None, None)
    room_list.append(room)

    room = Room("You're in a large stone hallway. You can hear water dripping."
                "\nThere are doors on the east and west walls"
                "\nThe door to the south leads to the chamber.", None, 13, 16, 17, None, None)
    room_list.append(room)

    room = Room("The room is very dark and damp. You see a large metal table in the center covered with blood."
                "\nThe chains attached to the ceiling are swaying slowly back and forth."
                "\nIt seems the only exit is back through the door, west.", None, None, None, 15, None, None)
    room_list.append(room)

    room = Room("There is a large sleeping bear blocking the exit to the south. It seems to be a cave."
                "\nThere is the doorway to hallway in the east.", None, None, 15, None, None, None)
    room_list.append(room)

    room = Room("It is a dark tunnel with a light at the end of it."
                "\nYou are sure you can get out if you keep going south. You can also go back north to the bear room.",
                17, 19, None, None, None, None)
    room_list.append(room)

    room = Room("You have finally escaped that creepy house."
                "\nThanks for playing!", None, None, None, None, None, None)
    room_list.append(room)

    item_list = []

    item = Item(5, "A short dull butter knife on the counter, good for spreading jam.", "Knife")
    item_list.append(item)

    item = Item(11, "There is one doll that is particularly shiny and well taken care of.", "Doll")
    item_list.append(item)

    item = Item(7, "A TV remote sits on the crusty couch.", "Remote")
    item_list.append(item)

    item = Item(4, "A book that reads 'How to be an efficient cannibal'.", "Book")
    item_list.append(item)

    item = Item(12, "A key on a hook, it looks to be like the skeleton variety.", "Key")
    item_list.append(item)

    item = Item(5, "There are a few pieces of questionable food in the refrigerator", "Food")
    item_list.append(item)

    item = Item(16, "A bloody cleaver stuck inside a block of wood.", "Cleaver")
    item_list.append(item)

    # Creating enemies to fight
    enemy_bear = Enemy("Bear", 50, random.randrange(4, 12), 17)
    enemy_man = Enemy("Man", 100, random.randrange(8, 21), 12)

    # Loading my sounds for combat
    player_got_hurt_sound = arcade.load_sound("hurt1.wav")

    enemy_got_hurt_sound = arcade.load_sound("hurt3.wav")

    current_room = 0
    done = False
    current_hp = 100

    print("Welcome to the House of Horror")
    print()
    print("You were walking on the street when you heard screams coming from inside the house.")
    print("Rushing into the house you shut the front door behind you.")
    print("You panic as you can no longer get the door open.")
    print("Good luck finding a way out.")

    while not done:

        # printing the current room description
        print(f"Current room: {current_room}")
        print()
        print(room_list[current_room].description)

        # If there is an item in the room print it
        for item in item_list:
            if item.room_number == current_room:
                print(item.long_description)

        print()
        print("You can type 'H' or 'help' for a full instruction of commands.")
        print()
        user_command = str(input("What would you like to do? "))
        command_words_list = user_command.split(" ")

        # This code handles the command words "Go" and "Travel" to move around the house.
        if command_words_list[0].upper() == "GO" and len(command_words_list) > 1 or \
                command_words_list[0].upper() == "TRAVEL" and len(command_words_list) > 1:
            if command_words_list[1].upper() == "N" or command_words_list[1].upper() == "NORTH":
                next_room = room_list[current_room].north
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            elif command_words_list[1].upper() == "S" or command_words_list[1].upper() == "SOUTH":
                next_room = room_list[current_room].south
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            elif command_words_list[1].upper() == "E" or command_words_list[1].upper() == "EAST":
                next_room = room_list[current_room].east
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            elif command_words_list[1].upper() == "W" or command_words_list[1].upper() == "WEST":
                next_room = room_list[current_room].west
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            elif command_words_list[1].upper() == "U" or command_words_list[1].upper() == "UP":
                next_room = room_list[current_room].up
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            elif command_words_list[1].upper() == "D" or command_words_list[1].upper() == "DOWN":
                next_room = room_list[current_room].down
                if next_room is None:
                    print("You can't go that way")
                else:
                    current_room = next_room
            else:
                print()
                print("I don't understand that.")

        # This controls for if you quit the game.
        if command_words_list[0].upper() == "Q" or command_words_list[0].upper() == "QUIT":
            print("Thanks for playing!")
            done = True

        # This command chain controls the ability to pick up items
        if command_words_list[0].upper() == "GET" or command_words_list[0].upper() == "GRAB":
            for item in item_list:
                if item.short_name.upper() == command_words_list[1].upper() and item.room_number == current_room:
                    item.room_number = -1
                    if item.short_name.upper() == "BOOK" and room_list[4].east != 13:
                        print("You hear a shifting and the bookcase slides out of the way"
                              " revealing stairs to the east.")
                        room_list[4].east = 13
                        room_list[4].down = 13
                        room_list[4].description = ("You stand in the office. There are two large brown chairs."
                                                    "\nThey haven't been used in a while."
                                                    "\nThere the a doorway to the west leading to the foyer."
                                                    "\nThe bookcase has now moved out of the way "
                                                    "and reveals stairs to the east.")

        # This command chain handles the inventory command
        if command_words_list[0].upper() == "INVENTORY" or command_words_list[0].upper() == "INV":
            for item in item_list:
                if item.room_number == -1:
                    print("You have", item.short_name)

        # This command chain handles dropping an item
        if command_words_list[0].upper() == "DROP":
            for item in item_list:
                if item.room_number == -1:
                    if command_words_list[1].upper() == item.short_name.upper():
                        item.room_number = current_room
                        print("You dropped the", item.short_name)
                    else:
                        print("I'm not sure what you want to drop.")

        # This command chain handles using objects
        if command_words_list[0].upper() == "USE":
            # Turns the TV on and off by changing the room description
            if command_words_list[1].upper() == "REMOTE" and item_list[2].room_number == -1:
                if room_list[7].description == ("You stand in the living room with the "
                                                "TV buzzing with black and white fuzz."
                                                "\nIt seems this place is real dusty."
                                                "\nTo the west is the kitchen and the east is a closet door."):
                    room_list[7].description = ("The TV is turned off now. You stand in living room."
                                                "\nIt's still incredibly dusty."
                                                "\nTo the west is the kitchen and the east is a closet door.")
                else:
                    room_list[7].description = ("You stand in the living room with the "
                                                "TV buzzing with black and white fuzz."
                                                "\nIt seems this place is real dusty."
                                                "\nTo the west is the kitchen and the east is a closet door.")

            if command_words_list[1].upper() == "KEY" and item_list[4].room_number == -1:
                if current_room == 5:
                    print("The freezer door unlocked.")
                    room_list[5].north = 6
                    print()
                    room_list[5].description = ("Standing in this very bloody and gross kitchen "
                                                "you wonder if anyone lives here."
                                                "\nTo the north is a large door that looks like a walk-in freezer,"
                                                " that is now unlocked."
                                                "\nTo the south is the dining room. East is the living room.")
                else:
                    print("You can't do that now.")

            if command_words_list[1].upper() == "DOLL" and item_list[1].room_number == -1:
                print("It seemed kind of pointless to take the doll."
                      "\nit is very shiny though.")

            if command_words_list[1].upper() == "FOOD" and item_list[5].room_number == -1:

                if current_room == 17:
                    print("You threw the food at the bear."
                          "\nIt ate the food and got out of the way.")
                    room_list[17].south = 19
                    room_list[17].description = ("The large bear is now out of the way in the corner."
                                                 "\nIt seems you are so close to freedom."
                                                 "\nThere is a door to the hallway to the east."
                                                 "\nThe cave is open to the south.")

                else:
                    print("You ate the food. You hope it will sit in your stomach well.")
                    item_list[5].room_number = -2

            if command_words_list[1].upper() == "BOOK" and item_list[3].room_number == -1:
                print("You begin reading from the book. The more you read the more disgusted you are."
                      "\nIt has very vivid descriptions about how to catch people and butcher them."
                      "\nYou decide to stop reading.")

            if command_words_list[1].upper() == "KNIFE" and item_list[0].room_number == -1:
                if current_room == 17:
                    print("You attempt to stab the bear with the small dull knife")
                    print("The bear attacked you and you are now dead.")
                    print("Thanks for playing, better luck next time.")
                    done = True
                else:
                    print("Not sure what you want to do with that.")

            if command_words_list[1].upper() == "CLEAVER" and item_list[6].room_number == -1:
                if current_room == 17:
                    print("You attempt to hack and slash at the bear."
                          "\nThrough a hectic battle you finally won and the bear is dead."
                          "\nOut of the way. You go south and escape from this hell hole.")
                    print("Thanks for playing.")
                    done = True
                else:
                    print("Not sure what you want to do with that.")

        if command_words_list[0].upper() == "H" or command_words_list[0].upper() == "HELP":
            print()
            print("You can type 'go' or 'travel' followed by the direction to move rooms. For example, "
                  "'go north' would move your player one room north if possible.")
            print()
            print("You can type 'get' or 'grab' to pick up an item. For example, "
                  "'get key' would add the key to your inventory.")
            print()
            print("You can type 'use [item]' to use the item in your inventory if possible.")
            print()
            print("You can type 'drop [item]' to place an item in a room.")
            print()
            print("You can type 'inventory' or 'inv' to see your current inventory.")
            print()
            print("You can type 'Q' or 'QUIT' to quit and end the game.")

        if current_room == 19:
            print(room_list[current_room].description)
            done = True

        if command_words_list[0].upper() == "FIGHT" and 1 < len(command_words_list) \
                or command_words_list[0].upper() == "F" and 1 < len(command_words_list):
            if command_words_list[1].upper() == "BEAR" and current_room == enemy_bear.room_number \
                    and enemy_bear.hp >= 0 or command_words_list[1].upper() == "B" \
                    and current_room == enemy_bear.room_number and enemy_bear.hp >= 0:
                fight_bear = True
                while fight_bear:
                    if enemy_bear.hp <= 0:
                        print("You killed the bear!")
                        room_list[17].description = ("You stand in a chamber. There is the hallway to the west."
                                                     "\nThe cave opening to the south. There is a dead bear.")
                        room_list[17].south = 19
                        enemy_bear.room_number = -2
                        fight_bear = False
                    print()
                    print("You are currently in a fight with the bear!")
                    print()
                    print("You can type 'h' or 'help' for the command list.")
                    print()
                    user_command = str(input("What would you like to do? "))
                    command_words_list = user_command.split(" ")

                    if command_words_list[0].upper() == "H" or command_words_list[0].upper() == "HELP":
                        print("In a fight you can type 'atk' or 'attack' "
                              "and the game will by default use your best weapon.")
                        print()
                        print("You can type 'run' or 'r', you will have a chance to escape.")
                        print()
                        print("You can type 'd' or 'dodge', the enemy attack has a greater chance not to hit you.")
                        print()
                        print("To win a fight you must bring the bear's hp down to 0.")

                    if command_words_list[0].upper() == "ATK" or command_words_list[0].upper() == "ATTACK":
                        chance_to_hit = random.randrange(1, 21)
                        if chance_to_hit > 13:

                            if item_list[6].room_number == -1:
                                print("You attacked with the cleaver!")
                                atk_dmg = random.randrange(10, 15)
                                enemy_bear.hp -= atk_dmg
                                arcade.play_sound(enemy_got_hurt_sound)
                                print(f"You dealt {atk_dmg} to the bear!")
                            elif item_list[0].room_number == -1:
                                print("You attacked with the butter knife!")
                                atk_dmg = random.randrange(5, 11)
                                enemy_bear.hp -= atk_dmg
                                arcade.play_sound(enemy_got_hurt_sound)
                                print(f"You dealt {atk_dmg} to the bear!")
                            else:
                                print("You attacked with a punch!")
                                atk_dmg = random.randrange(1, 7)
                                enemy_bear.hp -= atk_dmg
                                print(f"The dealt {atk_dmg} to the bear!")
                                arcade.play_sound(enemy_got_hurt_sound)
                        else:
                            print("You attacked and missed!")

                    if command_words_list[0].upper() == "R" or command_words_list[0].upper() == "Run":
                        chance_to_run = random.randrange(1, 21)
                        if chance_to_run > 10:
                            print("You successfully ran away!")
                            current_room -= 1
                            fight_bear = False
                        else:
                            print("You couldn't escape!")

                    chance_to_hit = random.randrange(1, 21)
                    if chance_to_hit > 10:
                        if command_words_list[0].upper() == "D" or command_words_list[0].upper() == "Dodge":
                            if chance_to_hit > 15:
                                print("The bear attacked you!")
                                current_hp -= random.randrange(2, 10)
                                arcade.play_sound(player_got_hurt_sound)
                            elif chance_to_hit <= 15:
                                print("The bear tried to attack you but missed!")
                        else:
                            print("The bear attacked you!")
                            atk_dmg = random.randrange(3, 10)
                            current_hp -= atk_dmg
                            print(f"The bear attacked you a dealt {atk_dmg} damage!")


"""
        # This checks to see if there is an enemy in the room, if there is initiate combat!
        for enemy in enemy_list:
            if enemy.room_number == current_room:
                currently_fight = True
                while currently_fight:
                    if enemy.hp <= 0:
                        print("You won the fight, congrats!")
                        currently_fight = False
                    print(f"You are in a fight with {enemy.name}!")
                    print()
                    print("You can type 'h' or 'help' for the command list.")
                    print()
                    user_command = str(input("What would you like to do? "))
                    command_words_list = user_command.split(" ")
                    if command_words_list[0].upper() == "H" or command_words_list[0].upper() == "HELP":
                        print("In a fight you can type 'atk' or 'attack' "
                              "and the game will by default use your best weapon.")
                        print()
                        print("You can type 'run' or 'r', you will have a chance to escape, varying on the enemy.")
                        print()
                        print("You can type 'd' or 'dodge', the enemy attack might not hit you.")
                        print()
                        print("Once you kill an enemy they will cease to exist.")

                    if command_words_list[0].upper() == "ATK" or command_words_list[0].upper() == "ATTACK":
                        if item_list[6].room_number == -1:
                            print("You attacked with the cleaver!")
                            enemy.hp -= random.randrange(10, 15)
                        elif item_list[0].room_number == -1:
                            print("You attacked with the butter knife!")
                            enemy.hp -= random.randrange(5, 11)
                        else:
                            print("You attacked with a punch.")
                            enemy.hp -= random.randrange(1, 7)

                    if command_words_list[0].upper() == "RUN" or command_words_list[0].upper() == "R":
                        run = random.randrange(0, 21)
                        if run >= 10:
                            print("You ran away")
                            currently_fight = False
                            current_room -= 1
                        else:
                            print("You tried to run away but it failed!")

                    print(f"{enemy.name} tried to attack you!")
                    print()
                    enemy_atk_roll = random.randrange(1, 21)
                    if enemy_atk_roll >= 13:
                        print(f"{enemy.name} attacked you!")
                        current_hp -= random.randrange(1, 21)
                        print(f"You now have {current_hp} hp left!")
                    else:
                        print(f"{enemy.name} missed their attack!")
"""

if __name__ == "__main__":
    main()
