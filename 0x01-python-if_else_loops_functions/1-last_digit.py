#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    cp = (number * -1) % 10
else:
    cp = number % 10
if (number < 0):
    cp *= -1
print("cp = {}".format(cp))
print("Last digit of {} is ".format(number), end='')
if cp > 5:
    print("{} and is greater than 5".format(cp))
elif cp == 0:
    print("{} and is 0".format(cp))
elif cp < 6:
    print("{} and is less than 6 and not 0".format(cp))
