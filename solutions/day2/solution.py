#!/usr/bin/python3

import sys

def isValid(numberString):
    if len(numberString) % 2 != 0:
        return True
    
    return numberString[:int(len(numberString)/2)] != numberString[int(len(numberString)/2):]

def getInvalidIds(low, high):
    i = low
    invalidIds = []

    while i <= high:
        if not isValid(str(i)):
            invalidIds.append(i)
        i += 1
    return invalidIds

print("Day 2 solution:")

rangeList = sys.stdin.read().strip().split(",")

range2dList = list(map(lambda x: x.split("-"),rangeList))

sumIds = 0

for _range in range2dList:
    for _id in getInvalidIds(int(_range[0]),int(_range[1])):
        sumIds += _id

print("Sum of invalid Ids: " + str(sumIds))
