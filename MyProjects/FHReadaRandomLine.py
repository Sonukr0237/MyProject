# 4.Write a Python program to read a random line from a file.
import random


def readRandomLine(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()

    randomLine = random.choice(lines)

    return randomLine.strip()

filePath = r'C:\Users\admin\OneDrive\Desktop\testText.txt'
randomLine = readRandomLine(filePath)
print('A random line from a file is : ', randomLine)

