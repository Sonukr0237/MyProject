# 3.Write a program to print sum, average of all numbers, smallest and largest element of a list.

varList = []

for i in range(10):
    while True:
        userInput = input(f'Input value for {i} index:')
        try:
            userInput = float(userInput)
            varList.append(userInput)
            break
        except ValueError:
            print('Invalid input, Please input a numeric value.')

print('List:', varList)

sumValues = sum(varList)
avg = sumValues/len(varList)

smallestNumber = varList[0]
for num in varList:
    if num < smallestNumber:
        smallestNumber = num

largestNumber = varList[0]
for num in varList:
    if num > largestNumber:
        largestNumber = num

print('The sum of these numbers: ', sumValues)
print('Average of these numbers : ', avg)
print('Smallest number in List : ', smallestNumber)
print('Largest number in List : ', largestNumber)