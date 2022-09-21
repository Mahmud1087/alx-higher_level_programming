#!/usr/bin/python3
def uppercase(str):
    for upper in range(0, len(str)):
        print("{:c}".format(ord(str[upper])-32)
                if ord(str[upper]) in range(ord('a'), ord('z')+1)
                else str[upper], end='')
    print()
