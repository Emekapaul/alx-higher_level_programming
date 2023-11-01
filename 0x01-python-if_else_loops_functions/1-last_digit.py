#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

conv = abs(number)
ldig = conv % 10

if (ldig > 5):
    print(f'Last digit of {number} is {ldig} and is greater than 5')

elif (ldig == 0):
    print(f'Last digit of {number} is {ldig} and is 0')

else:
    print(f'Last digit of {number} is {ldig} and is less than 6 and not 0')
