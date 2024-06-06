# Write a Python program to remove a key from a dictionary.

def getDictInput():

    dictionary = {}
    while True:
        key = input("Enter Key (or done to finish):")
        if key.lower() == "done":
            break
        value = input("Enter Value:")
        dictionary[key] = value

    return dictionary

def removeKeyFromDictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"key {key} has been removed.")
    else:
        print(f"key {key} not found in the dictionary.")

    return dictionary

print("Enter the dictionary:")
userDictionary = getDictInput()

print("\nOriginal Dictionary:")
print(userDictionary)

keyToRemove = input("Enter the key want to remove:")

updatedDictionary = removeKeyFromDictionary(userDictionary, keyToRemove)

print("Updated dictionary:")
print(updatedDictionary)

