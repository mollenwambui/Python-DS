#Write a Python function to multiply all the numbers in a list
from itertools import product


def multiply_all_numbers(*numbers):
    product=1
    for x in numbers:
          product*=x
    return product