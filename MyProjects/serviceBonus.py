salary = float(input('Enter your salary : '))
totalYear = float(input('Enter total number of working years : '))
if(totalYear > 5):
    bonus = 5 / 100 * salary
    print('your bonus amount is', bonus)
else:
    print('You are not eligible for bonus.')
