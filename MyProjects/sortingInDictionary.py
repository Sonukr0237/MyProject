# Write a Python program to sort a given dictionary by key
#

from removingKeyFromDict import getDictInput

def sortDictionaryByKey(dictionary):

    sortedDictionary = dict(sorted(dictionary.items()))
    return sortedDictionary

print("Enter the dictionary:")
userDictionary = getDictInput()

print("Original Dictionary:")
print(userDictionary)

sortedDictionary = sortDictionaryByKey(userDictionary)

print("Sorted Dictionary by Key:")
print(sortedDictionary)