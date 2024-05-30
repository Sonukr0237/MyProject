number = int(input('Enter the number: '))

reversedNumber = 0
while number >0:
    digit = number % 10
    reversedNumber = reversedNumber * 10 + digit
    number = number // 10

print('Reversed Number is ', reversedNumber)