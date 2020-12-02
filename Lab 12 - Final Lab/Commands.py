def ask_the_user():
    """This is the function to ask to user what they want to do in-game."""

    # Storing what the player types as a string.
    user_commands = str(input("What would you like to do? "))

    # Split the user_command into a list the computer can process.
    command_words = user_commands.split(" ")

    return command_words


ask_the_user()
