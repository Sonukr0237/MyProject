# Write a Python program to check multiple keys exists in a dictionary.

from removingKeyFromDict import getDictInput

def checkKeyExist(dictionary, keys):
    missingKeys = [key for key in keys if key not in dictionary]
    if not missingKeys:
        return True, None
    return False, missingKeys

print("Enter the Dictionary:")
userDictionary = getDictInput()

print("Original Dictionary:")
print(userDictionary)

keysToCheck = input("Enter the keys to check (comma-seperated):").split(',')

keysToCheck = [key.strip() for key in keysToCheck]

allKeysExist, missingKeys = checkKeyExist(userDictionary, keysToCheck)

if allKeysExist:
    print("All key exist in the dictionary.")
else:
    print(f"The following keys are missing: {', '.join(missingKeys)}")
