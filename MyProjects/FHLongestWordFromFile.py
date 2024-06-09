# Write a python program to find the longest words in a file.

def findLongestWords(filePath):
    with open(filePath, 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    words = [word.strip('.,!?";:(){}[]') for word in words]

    maxLength = max(len(word) for word in words)

    longestWords = [word for word in words if len(word) == maxLength]

    return longestWords

filePath = r'C:\Users\admin\OneDrive\Desktop\testText.txt'
longestWords = findLongestWords(filePath)
print("The longest words are:", longestWords)
