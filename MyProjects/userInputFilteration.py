# 2.Take 20 integer inputs from user and print the following:
#
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.


var_list = []

for i in range(20):
    while True:
        userInput = input(f'input value for {i} index :')
        try:
            userInput = float(userInput)
            var_list.append(userInput)
            break
        except ValueError:
            print("Invalid input, Plese enter a numeric value.")

print('List:', var_list)
positiveNumber = 0
negativeNumber = 0
oddNumber = 0
evenNumber = 0
zeros = 0

for num in var_list:
    if num > 0:
        positiveNumber += 1
    elif num < 0:
        negativeNumber +=1
    else:
        zeros += 1

    if num % 2 == 0:
        evenNumber += 1
    else:
        oddNumber += 1


print('Number of positive numbers : ', positiveNumber)
print('Number of negative numbers :', negativeNumber)
print('Number of odd numbers :', oddNumber)
print('Number of even numbers :', evenNumber)
print('Number of Zeros :', zeros)