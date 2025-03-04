#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 19, 2025

# This program calculates the area and circumference of
# a circle using a modified version of archimedes' pi
# approximation based on user input


import math

# array to store startup messages
MESSAGES_TO_PRINT = [
    """
    Welcome to Jack's Pi Approximation tool, 
    a tool used for approximating pi and calculating 
    the circumference and area of a circle from it.
    """,

    """
    To start, please enter the approximation for pi 
    (3-1,000,000 and must be an integer):""",
    """
    Now please enter your radius (cm - float number):
    """,
    
    """
    How many decimals do you want to round it to? (Integer 1-12)
    """,
]


def get_pi_approx(iterations):
    if iterations and iterations >= 3 and iterations <= 10000000:

        # get inner angle of theoretical tri
        inner_angle = 360 / iterations
        # get outer angle of theoretical tri
        outer_angle = (180 - inner_angle) / 2
        # get side length (pi approx * 2 / iterations)
        outer_side_length = math.sin(math.radians(inner_angle)) / math.sin(
            math.radians(outer_angle)
        )
        # calculate pi approximation
        pi_approx = outer_side_length * iterations / 2
        return pi_approx  # Return pi approximation
    else:
        return 0  # Return 0 if wrong user input


def main():

    # Set all variables
    round_to_place = 0
    radius = 0.0
    pi_approx = 0
    margin_of_error = 0

    for i in range(1, 5):
        print(
            MESSAGES_TO_PRINT[i - 1]
        )  # Print message at i index for messages to print array
        if i == 2:
            pi_approx = int(input())  # Ask for pi approx iterations
        if i == 3:
            radius = float(input())  # Ask for radius
        if i == 4:
            round_to_place = int(input())  # Ask for round to place

    pi_approx = get_pi_approx(pi_approx)  # pi approximation from pi approximation func
    if pi_approx > 0:
        margin_of_error = (
            100 * (math.pi / pi_approx) - 100
        )  # Margin of error as num from 0-100

    if pi_approx > 0:
        # Create messages for each piece of data to display
        output1 = (
            "The circumference of your circle is "
            + str(round(pi_approx * 2 * radius, round_to_place))
            + " cm"
        )
        output2 = (
            "The area of your circle is "
            + str(round(pi_approx * (radius**2), round_to_place))
            + " cm^2"
        )
        output3 = (
            "The margin of error for your pi approximation was "
            + str(margin_of_error)
            + "%"
        )
        print(output1)  # Print circ.
        print(output2)  # Print area.
        print(output3)  # Print margin of error.

    else:  # Data entered improperly
        print("Please make sure to enter valid numbers")  # Warning msg
        main()  # Restart the main function if user improperly entered data


if __name__ == "__main__":
    main()  # Fire main function, initiate the program
