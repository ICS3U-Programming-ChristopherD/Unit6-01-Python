#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Dec.14, 2022
# This program generates 10 random numbers and
# calculates their average

import random
import constants


def main():
    # Creates an empty list to store the random numbers
    random_numbers = []
    sum = 0

    # For loop generates ten random numbers from 1-100
    for counter in range(constants.MAX_ARRAY_SIZE):

        # Generates random number from 1-100
        random_int = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Adds random number to list
        random_numbers.append(random_int)

        print(f"Added {random_int} to list at index {counter}")

        # Adds the value of the number to sum
        sum += random_int

    # Prints the average of the ten numbers
    print(f"The average of the {constants.MAX_ARRAY_SIZE} numbers is {sum/2}.")


if __name__ == "__main__":
    main()
