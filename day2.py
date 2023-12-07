import sys

inputs = []

def parseInputs(fname: str):
    with open(fname,"r") as f:
        for line in f:
            inputs.append(line)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        fname = "smallTest.txt"
    else:
        fname = sys.argv[1]