def greatestNumber(numbers):
    if not numbers:
        print('Enter the valid numbers')
        return None

    greatest = numbers[0]

    for number in numbers:
        if number > greatest:
            greatest = number

    return greatest

while True:
    input_string = input("Enter numbers separated by spaces: ")

    try:
        numbers = [int(num) for num in input_string.split()]
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        numbers = []


    num = greatestNumber(numbers)
    if num is not None:
        print("The greatest number is:", num)



def greatestDigit(dig):
    res = max(dig)
    return res

dig = [3,2,5,3,7,77,87,67,56,76,89,54]
result = greatestDigit(dig)

print('Maximum number is', result)