# Write a function to calculate area and circumference of a circle

import math


def circleProperties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius

    return {
        "area": area,
        "circumference": circumference
    }

def getNumericInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter only numeric value.")

radius = getNumericInput("Enter the Radius of Circle:")


properties = circleProperties(radius)

print(f"Area : {properties['area']}")
print(f"Circumference : {properties['circumference']}")