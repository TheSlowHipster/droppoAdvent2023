import sys
from typing import Tuple


DIGIT_STRINGS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

inputs = []

def parseInputs(fname: str):
    with open(fname,"r") as f:
        for line in f:
            inputs.append(line)

def atoi(character: str) -> int:
    return (ord(character) - 48)

def findValueInt(line: str) -> int:
    value = 0
    foundFirst = False
    idx = 0
    while not foundFirst and idx < len(line) - 1:
        if line[idx].isdigit():
            value += 10*atoi(line[idx])
            foundFirst = True
        idx += 1
    idx = len(line) - 1
    foundLast = False
    while not foundLast and idx >= 0:
        if line[idx].isdigit():
            value += atoi(line[idx])
            foundLast = True
        idx -= 1
    return value

def getDigitForwards(line: str, idx: int, digit: str) -> Tuple[bool, int]:
    tmpIdx = idx
    test = line[idx]
    while tmpIdx < len(line) - 2 and test in digit:
        tmpIdx+=1
        test += line[tmpIdx]
    if test[:-1] == digit:
        #print(f"Forwards found {test}\nChecking for: {digit}")
        #print("Passed")
        return True, DIGIT_STRINGS.index(digit)
    else:
        return False, 0

def getDigitBackwards(line: str, idx: int, digit: str) -> Tuple[bool, int]:
    tmpIdx = idx
    test = line[idx]
    while tmpIdx >= 0 and test in digit:
        tmpIdx -= 1
        test = line[tmpIdx] + test
    if test[1:] == digit:
        return True, DIGIT_STRINGS.index(digit)
    else:
        return False, 0

def findValueStr(line: str) -> int:
    value: int = 0
    idx: int = 0
    foundFirst: bool = False
    while not foundFirst and idx < len(line) - 1:
        if line[idx].isdigit():
            value += 10 * atoi(line[idx])
            foundFirst = True
        else:
            for digit in DIGIT_STRINGS:
                if line[idx] in digit and not foundFirst:
                    foundFirst, tmpVal: int = getDigitForwards(line, idx, digit)
                    if foundFirst:
                        value += 10 * tmpVal
        idx += 1

    idx = len(line) - 1
    foundLast: bool = False
    while not foundLast and idx >= 0:
        if line[idx].isdigit():
            value += atoi(line[idx])
            foundLast = True
        else:
            for digit in DIGIT_STRINGS:
                if line[idx] in digit and not foundLast:
                    foundLast, tmpVal: int = getDigitBackwards(line, idx, digit)
                    if foundLast:
                        value += tmpVal
        idx -= 1
    print(f"Value found: {value}\n")
    return value

def sumValuesInt() -> int:
    sum = 0
    for line in inputs:
        print(findValueInt(line))
        sum += findValueInt(line)
    return sum

def sumValuesStr() -> int:
    sum = 0
    for line in inputs:
        # print(findValueStr(line))
        sum += findValueStr(line)
    return sum

if __name__ == "__main__":
    if len(sys.argv) < 2:
        fname = "smallTest.txt"
    else:
        fname = sys.argv[1]
    parseInputs(fname)
    # print(sumValuesInt())
    print(sumValuesStr())