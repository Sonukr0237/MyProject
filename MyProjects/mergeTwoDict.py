# myDict = {}
#
# for i in range(5):
#     k = input("Enter Key : ")
#     v = input("Enter Values : ")
#
#     myDict[k] = v
#
# print(myDict)

# Write a Python script to merge two Python dictionaries


def getDictionaryInput(prompt):
    print(prompt)

    dictionary = {}
    while True:
        key = input("Enter key (or done to finish):")
        if key.lower() == 'done':
            break
        value = input("Enter Value:")
        dictionary[key] = value

    return dictionary

def mergeDictionaries(dict1, dict2):
    mergeDict = {**dict1, **dict2}
    return mergeDict

print("Enter First Dictionary : ")
dict1 = getDictionaryInput("Input Key-Value pairs for the first dictionary. Type 'done' to finish.")

print("Enter Second Dictionary : ")
dict2 = getDictionaryInput("Input Key-Value pairs for the first dictionary. Type 'done' to finish.")

mergedDict = mergeDictionaries(dict1, dict2)
print("\n The merged dictionary is : ")

print(mergedDict)
