import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():

    dictionary = open("dictionary.txt")

    dictionary_word_list = []

    for line in dictionary:

        line = line.strip()

        dictionary_word_list.append(line)

    dictionary.close()

    print("---Linear Search---")

    alice_in_wonderland = open("AliceInWonderLand200.txt")

    alice_line_location = 0

    for line in alice_in_wonderland:

        alice_line_location += 1

        alice_word_list = split_line(line)

        for word in alice_word_list:

            # Start at the beginning of the list
            current_dictionary_list_position = 0

            # Loop until you reach the end of the list, or the value at the
            # current position is equal to the key
            while current_dictionary_list_position < len(dictionary_word_list) and \
                    dictionary_word_list[current_dictionary_list_position] != word.upper():

                # Go to the next word in the dictionary
                current_dictionary_list_position += 1
            if current_dictionary_list_position == len(dictionary_word_list):
                print("This word was not in the dictionary: ", word, "on line", alice_line_location)

    alice_in_wonderland.close()

    print("---Binary Search---")

    alice_in_wonderland = open("AliceInWonderLand200.txt")

    alice_line_location = 0

    for line in alice_in_wonderland:

        alice_word_list = split_line(line)

        alice_line_location += 1

        for word in alice_word_list:

            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_word_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                # Find the middle position
                middle_pos = (lower_bound + upper_bound) // 2

                # Figure out if we:
                # move up the lower bound, or
                # move down the upper bound, or
                # we found what we are looking for
                if dictionary_word_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_word_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("The word: ", word, "on line", alice_line_location, "may be spelled wrong.")

    alice_in_wonderland.close()


main()
