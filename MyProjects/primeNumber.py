# 5.Write a function to check if a number is prime or not.

def prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            if number % i == 0:
                return False
        return True

def userInput():
    try:
        number = int(input("Enter a number: "))
        if prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Enter a valid integer.")

userInput()
