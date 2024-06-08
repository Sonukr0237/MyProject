# Print multiplication table of user input number by using recursion.


def multiplicationTable(number, multiplier = 1, limit = 10):
    if multiplier > limit:
        return

    print(f"{number} * {multiplier} = {number * multiplier}")

    multiplicationTable(number, multiplier + 1, limit)

def onlyNumericValue(prompt = "Enter a num :"):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter a number.")

num = onlyNumericValue()
multiplicationTable(num)