# 5.Write a Python program to count the number of lines in a text file.
def countLineinFiles(filePath):

    with open(filePath, 'r') as file:
        lines = file.readlines()

    numberofLines = len(lines)

    return numberofLines


filePath = r'C:\Users\admin\OneDrive\Desktop\testText.txt'

lineCount = countLineinFiles(filePath)

print("The count of lines in file is :", lineCount)