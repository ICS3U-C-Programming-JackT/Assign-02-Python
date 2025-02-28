#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: February 19, 2025

# This program calculates the area and circumference of
# a circle using a modified version of archimedes' pi 
# approximation based on user input


import math

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
];

def get_pi_approx(iterations):
    if iterations and iterations>=3 and iterations<=10000000:
        inner_angle = 360/iterations;
        outer_angle = (180-inner_angle)/2;
        outer_side_length = math.sin(math.radians(inner_angle))/math.sin(math.radians(outer_angle));
        pi_approx = outer_side_length*iterations/2;
        return pi_approx;
    else:
        return 0;

def main():

    round_to_place = 0;
    radius = 0.0;
    pi_approx = 0;
    margin_of_error = 0;

    for i in range(1,5):
        print(MESSAGES_TO_PRINT[i-1])
        if i==2:
            pi_approx = int(input());
        if i==3:
            radius = float(input());
        if i==4:
            round_to_place = int(input());
    
    pi_approx = get_pi_approx(pi_approx);
    margin_of_error = 100*(math.pi/pi_approx)-100

    if pi_approx>0:

        output1 = "The circumference of your circle is "+str(round(pi_approx*2*radius,round_to_place))+" cm";
        output2 = "The area of your circle is "+str(round(pi_approx*(radius**2),round_to_place))+" cm^2";
        output3 = "The margin of error for your pi approximation was "+str(margin_of_error)+"%"
        print(output1);
        print(output2);
        print(output3);
    
    else: 
       print("Please make sure to enter valid numbers");
       main();



if __name__ == "__main__":
    main();
