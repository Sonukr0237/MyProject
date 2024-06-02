# 4.Make a list by taking 10 input from user. Now delete all repeated elements of the list.
# E.g.-
# INPUT : [1,2,3,2,1,3,12,12,32]
# OUTPUT : [1,2,3,12,32]

varList = []

for i in range(10):
    while True:
        userInput = input(f'Input value for {i} index : ')
        try:
            userInput = float(userInput)
            varList.append(userInput)
            break
        except ValueError:
            print('Invalid input, Enter a numeric value')

uniqueList = []
for num in varList:
    if num not in uniqueList:
        uniqueList.append(num)


print('List :', varList)
print('After removing duplicate values :', uniqueList)
