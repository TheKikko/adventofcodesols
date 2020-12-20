# Day 1 in advent of code 2020

inputfile = open("day1input.txt", 'r')


inputs = list(map(int,inputfile.read().split())) # gives a list of integers


def findNum(num, inputs):
    for number in inputs:
        sums = list(map(lambda x: number + x, inputs)) # finds the sum of current number + all others
        if num in sums:
            otherNumber = inputs[sums.index(2020)]
            return number * otherNumber

def findNumPt2(num, inputs):
    # trying the brute force bc I'm tired
    for number1 in inputs:
        for number2 in inputs:
            for number3 in inputs:
                if number1 + number2 + number3 == num:
                    return number1 * number2 * number3

print(findNum(2020,inputs))
print(findNumPt2(2020,inputs))
