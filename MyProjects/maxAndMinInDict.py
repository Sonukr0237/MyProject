
# Write a Python program to get the maximum and minimum value in a dictionary.

def getDictionaryInput():
    dictionary = {}
    while True:
        key = input("Enter the key (or 'done' to finish):")
        if key.lower() == 'done':
            break

        value = input("Enter the value:")
        try:
            dictionary[key] = float(value)
        except ValueError:
            print("PLease enter a valid number for value.")
    return dictionary


def findMaxMinValues(dictionary):
    if not dictionary:
        return None, None
    maxValue = max(dictionary.values())
    minValue = min(dictionary.values())
    return maxValue, minValue

print("Enter the dictionary:")
userDict = getDictionaryInput()

print("Original Dictionary:")
print(userDict)

maxValue, minValue = findMaxMinValues(userDict)

if maxValue is not None and minValue is not None:
    print(f"Maximum Value: {maxValue}")
    print(f"Minimum Value: {minValue}")
else:
    print("The dictionary is empty.")
