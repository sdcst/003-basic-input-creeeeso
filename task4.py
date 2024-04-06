#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
radius=int(input("What is the radius of your cone? "))
height=int(input("What is the height of your cone? "))

surfacearea=math.pi* radius *(radius+ ( (height**2) +(radius**2))**0.5)

print(f"Your surface area is {surfacearea}")