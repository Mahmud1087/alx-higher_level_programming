#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = number % 10 if number > 10 else number*-1 % 10
    print("{:d}".format(lastdigit), end='')
    return lastdigit
