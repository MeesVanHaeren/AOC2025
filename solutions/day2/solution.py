#!/usr/bin/python3

import sys

def isInvalid(numberString):
    return len(numberString) % 2 != 0 or numberString[:int(len(numberString)/2)] == numberString[int(len(numberString)/2):]
