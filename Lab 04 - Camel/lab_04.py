import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print()

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    distance_natives_traveled = -20
    drinks_in_canteen = 3

    done = False
    while not done:
        print()
        print("A. Drink from your canteen")
        print("B. Ahead at a moderate speed")
        print("C. Ahead at full speed.")
        print("D. Stop for the night.")
        print("E. Status check")
        print("Q. Quit.")
        print()
        answer = input("What is your choice? ")

        if answer.lower() == "q":
            # Quitting the game
            print()
            print("You have given up.")
            print("Thanks for playing!")
            done = True

        elif answer.lower() == "e":
            # Checking status of the player
            print()
            print("You have traveled", miles_traveled, "miles.")
            print("You have", drinks_in_canteen, "drinks of water left.")
            if miles_traveled > 0:
                print("The natives are", miles_traveled - distance_natives_traveled, "miles behind you!")
            else:
                print("The natives are behind you!")

        elif answer.lower() == "d":
            # Rest for the night
            print()
            camel_tiredness = 0
            print("The camel is happy!")
            distance_natives_traveled += random.randrange(7, 15)
            if (miles_traveled - distance_natives_traveled) >= 0:
                if distance_natives_traveled <= 0:
                    print("The natives are behind you!")
                else:
                    print("The natives are now", miles_traveled - distance_natives_traveled, "miles behind you!")

        elif answer.lower() == "c":
            # Travelling ahead at full speed
            print()
            print("You went ahead at full speed!")
            random_number = random.randrange(10, 21)
            miles_traveled += random_number
            print("You traveled", random_number, "miles.")
            if not done:
                if miles_traveled >= 200:
                    print("Congratulations, you have crossed the Mobi desert!")
                    print("Thanks for playing!")
                    done = True
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            if not done:
                distance_natives_traveled += random.randrange(7, 15)
                print("The natives are", miles_traveled - distance_natives_traveled, "behind you!")

            # Random oasis event while travelling.
                if random.randrange(20) == 0:
                    print("You found an oasis!")
                    print("Your canteen has been fully filled.")
                    print("You and your camel are well rested!")
                    camel_tiredness = 0
                    drinks_in_canteen = 3
                    thirst = 0

        elif answer.lower() == "b":
            # Riding the camel at a moderate pace.
            print()
            print("You went ahead at a moderate speed!")
            random_number = random.randrange(5, 13)
            miles_traveled += random_number
            print("You have traveled", random_number, "miles.")
            if not done:
                if miles_traveled >= 200:
                    print("Congratulations, you have crossed the Mobi desert!")
                    print("Thanks for playing!")
                    done = True
            thirst += 1
            camel_tiredness += 1
            if not done:
                distance_natives_traveled += random.randrange(7, 15)
                print("The natives are", miles_traveled - distance_natives_traveled, "behind you!")

            # Random oasis event.
                if random.randrange(20) == 0:
                    print("You found an oasis!")
                    print("Your canteen has been fully filled.")
                    print("You and your camel are well rested!")
                    camel_tiredness = 0
                    drinks_in_canteen = 3
                    thirst = 0

        elif answer.lower() == "a":
            # Drinking from the canteen.
            print()
            if drinks_in_canteen <= 0:
                print("Oh no! You have no more water!")
            else:
                print("You drank from your canteen.")
                print("You have", drinks_in_canteen, "left.")
            drinks_in_canteen -= 1
            thirst = 0

        if not done:
            if 6 >= thirst >= 4:
                print("You are thirsty.")
            elif thirst > 6:
                print("You died from thirst!")
                print("Game Over, try again.")
                done = True

        if not done:
            if 8 >= camel_tiredness >= 5:
                print("Your camel is getting tired.")
            elif camel_tiredness > 8:
                print("You pushed you camel too hard!")
                print("Your camel is now dead, and so are you!")
                done = True

        if not done:
            # If statement to see how far back the natives are.
            if distance_natives_traveled >= miles_traveled:
                print("The natives have caught up and killed you!")
                print("Game over, please try again.")
                done = True

        if not done:
            if (miles_traveled - distance_natives_traveled) < 15:
                print("The natives are getting close!")


if __name__ == main():
    main()
