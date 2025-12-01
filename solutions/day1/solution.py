#!/usr/bin/python3

import sys

class rotation:
    def __init__(self, result, zeros):
        self.result = result
        self.zeros = zeros
    def __repr__(self):
        return f"Result position:{self.result}, zeroes hit:{self.zeros}"

def rotate(current, direction, amount):
    resultRotation = rotation(0,0)
    rotated = 0

    step = 1
    if  direction == "L":
        step = -1

    while rotated < amount:
        rotated += 1
        current += step
        if current == 100:
            current = 0
        if current == -1:
            current = 99

        if current == 0:
            resultRotation.zeros += 1

    resultRotation.result = current
    return resultRotation

print("Day 1 solution:")
currentDigit = 50

allpositions = []

for item in sys.stdin:
    item = item.strip()
    newRotation = rotate(currentDigit,item[0], int(item[1:]))
    allpositions.append(newRotation)
    currentDigit = newRotation.result

zeroPositionCount = 0
zeroHitCount = 0
for position in allpositions:
    if position.result == 0:
        zeroPositionCount += 1
    zeroHitCount += position.zeros
    
print("Amount of zero positions: " + str(zeroPositionCount))
print("Amount of zero hits: " + str(zeroHitCount))
