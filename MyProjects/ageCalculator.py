from datetime import date


def ageCalculation(year):
    result = date.today().year - year
    return result

try:
    value = int(input("Enter a value: "))
    if value > date.today().year or value < 0:
        print("Enter a Valid birth year.")
    else:
            result = ageCalculation(value)
            print(f"Your age is : {result}")
except ValueError:
    print("Please enter a valid numeric value.")

