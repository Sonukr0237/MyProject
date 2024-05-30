def add(x, y):
    """Function to add two numbers"""
    return x+y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x-y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x*y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error! Division by Zero."
    else:
        return x/y

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter Choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        firstNumber = float(input("Enter first number : "))
        secondNumber = float(input("Enter second number : "))

        if choice == '1':
            print("Result:", add(firstNumber, secondNumber))
        elif choice == '2':
            print("Result:", subtract(firstNumber, secondNumber))
        elif choice == '3':
            print("Result:", multiply(firstNumber, secondNumber))
        elif choice == '4':
            print("Result:", divide(firstNumber, secondNumber))
        break

    else:
        print('Invalid Input')


