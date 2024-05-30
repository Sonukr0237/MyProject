number = [1, 8,4 ,3, 5, 3, 6, 23, 43, 44, 12, 100, 103,104, 105]
even_num = []

for i in number:
    if(i%2 == 0):
        even_num.append(i)

print(even_num)





# or we can also do in this way
even_num = [i for i in number if(i%2==0)]

print(even_num)