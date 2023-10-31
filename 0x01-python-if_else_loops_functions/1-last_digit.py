#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less_than_6 = "and is less than 6 and not 0"
great_than_5 = "and is greater than 5"

if number >= 0:
    last_digit = number % 10
else:
    last_digit = (-number % 10)

if last_digit > 5:
    print("Last digit of {} is {} {}".format(number, last_digit, great_than_5))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit))
elif (last_digit < 6) and (not (last_digit == 0)):
    print("Last digit of {} is {} {}".format(number, last_digit, less_than_6))
