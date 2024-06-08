# 4.Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(number):
    factors = [i for i in range(1, number) if number%i == 0]
    return sum(factors) == number

def perfectNumber(limit):
    for num in range(1, limit + 1):
        if perfect(num):
            print(num)


perfectNumber(1000)