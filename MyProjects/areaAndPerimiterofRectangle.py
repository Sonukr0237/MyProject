def rectangleProperties(length, breadth):
    area = length * breadth
    perimeter = 2 * (length * breadth)
    return {
        'area': area,
        'perimeter': perimeter
    }

def getNumericInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Enter a Numeric value.")

length = getNumericInput("Enter the legth of rectangles:")
breadth = getNumericInput("Enter the breadth of rectangle:")

properties = rectangleProperties(length, breadth)

print(f"Area: {properties['area']}")
print(f"Perimeter: {properties['perimeter']}")
