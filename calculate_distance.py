#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg
from math import sqrt

# decoration
print(stylize("\n---- | Calculate the distance between two points | ----\n", fg("red")))

# user interaction
first_point = input("Please enter the first point (x, y): ").split(", ")
second_point = input("Please enter the second point (x, y): ").split(", ")

# main program
def calculate_distance(point1, point2):
    # pythagorean theorem
    a = 0
    b = 0

    a += abs(float(point1[0])-float(point2[0]))
    b += abs(float(point1[1])-float(point2[1]))

    return sqrt(a**2 + b**2)

distance = stylize(str(round(calculate_distance(first_point, second_point), 3)), fg("red"))
print(f"\nThe distance between P1{float(first_point[0]), float(first_point[1])} and P2{float(second_point[0]), float(second_point[1])} is: {distance}.\n")
