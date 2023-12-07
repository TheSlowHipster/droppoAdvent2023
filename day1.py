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

"""
Create a list of inputs stored globally
"""
def parseInputs(fname: str):
    with open(fname,"r") as f:
        for line in f:
            inputs.append(line)

"""
Return the int value of a digit character (assumed to be first in string)
"""
def atoi(character: str) -> int:
    return (ord(character[0]) - 48)

"""
Iterates through the first and last indices to find single digit integers to
  generate a two-digit result
"""
def findValueInt(line: str) -> int:
    value = 0
    foundFirst = False
    idx = 0

    # Invariant: First integer hasn't been found and more line remains
    while not foundFirst and idx < len(line) - 1:
        # If the current character is a digit it becomes the 10s place
        if line[idx].isdigit():
            value += 10*atoi(line[idx])
            foundFirst = True
        idx += 1

    # Reset the index to end of the line
    idx = len(line) - 1
    foundLast = False

    # Invariant: Last integer hasn't been found and more line remains
    while not foundLast and idx >= 0:
        # If the current character is a digit it becomes the 1s place
        if line[idx].isdigit():
            value += atoi(line[idx])
            foundLast = True
        idx -= 1
    
    # Return the found value
    return value

"""
Iterates through a string starting at idx appending characters until either the
  digit was found or the substring no longer matches the digit being searched.
"""
def getDigitForwards(line: str, idx: int, digit: str) -> Tuple[bool, int]:
    tmpIdx = idx
    test = line[idx]
    # Invariant: test is a substring of digit
    while tmpIdx < len(line) - 2 and test in digit:
        tmpIdx+=1
        test += line[tmpIdx]
    # Test is either digit & an extra char or it isn't the digit
    if test[:-1] == digit:
        return True, DIGIT_STRINGS.index(digit)
    else:
        return False, 0

"""
Iterates through a string starting at idx prepending characters until either the
  digit was found or the substring no longer matches the digit searched.
"""
def getDigitBackwards(line: str, idx: int, digit: str) -> Tuple[bool, int]:
    tmpIdx = idx
    test = line[idx]
    # Invariant: test is a substring of digit
    while tmpIdx >= 0 and test in digit:
        tmpIdx -= 1
        test = line[tmpIdx] + test
    # Test is either digit & an extra char or it isn't the digit
    if test[1:] == digit:
        return True, DIGIT_STRINGS.index(digit)
    else:
        return False, 0


"""
Iterates through the first and last indices to find single digit integers or
  their word representations to generate a two-digit result
"""
def findValueStr(line: str) -> int:
    value: int = 0
    idx: int = 0
    foundFirst: bool = False
    # Invariant: First integer hasn't been found and more line remains
    while not foundFirst and idx < len(line) - 1:
        # If it's a digit we're done
        if line[idx].isdigit():
            value += 10 * atoi(line[idx])
            foundFirst = True
        # Else we need to parse for a digit substring
        else:
            for digit in DIGIT_STRINGS:
                if line[idx] in digit and not foundFirst:
                    foundFirst, tmpVal: int = getDigitForwards(line, idx, digit)
                    if foundFirst:
                        value += 10 * tmpVal
        idx += 1

    idx = len(line) - 1
    foundLast: bool = False
    # Invariant: Last integer hasn't been found and more line remains
    while not foundLast and idx >= 0:
        # If it's a digit we're done
        if line[idx].isdigit():
            value += atoi(line[idx])
            foundLast = True
        # Else we need to parse for a digit substring
        else:
            for digit in DIGIT_STRINGS:
                if line[idx] in digit and not foundLast:
                    foundLast, tmpVal: int = getDigitBackwards(line, idx, digit)
                    if foundLast:
                        value += tmpVal
        idx -= 1
    print(f"Value found: {value}\n")
    return value

"""
Finds the sum of all two-digit integers found by the rules of the A part of the
  puzzle
"""
def sumValuesInt() -> int:
    sum = 0
    for line in inputs:
        sum += findValueInt(line)
    return sum

"""
Finds the sum of all two-digit integers found by the rules of the B part of the
  puzzle
"""
def sumValuesStr() -> int:
    sum = 0
    for line in inputs:
        sum += findValueStr(line)
    return sum

"""
Main functionality
"""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        fname = "smallTest1.txt"
    else:
        fname = sys.argv[1]
    parseInputs(fname)
    print(sumValuesInt())
    print(sumValuesStr())