def power_of_100(value):
    result = value**100
    return result

try:
    value = float(input("Enter a value: "))
    result = power_of_100(value)
    print(f"{value} raised to the power 100 is : {result}")
except ValueError:
    print("Please enter a valid numeric value.")
