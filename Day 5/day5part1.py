import os, sys

with open(os.path.join(sys.path[0], "day5input.txt")) as file:
    passes = file.read().splitlines()

def find(bpass, index, min, max):
    # F/L = lower half, B/R = upper half
    diff = (max + 1) - min
    if bpass[index] == "F" or bpass[index] == "L":
        if diff == 2:
            return min
        return find(bpass, index + 1, min, max - diff/2)
    else: # == "B" or "R":
        if diff == 2:
            return max
        return find(bpass, index + 1, min + diff/2, max)

# main
ids = []
for bpass in passes:
    ids.append((int(find(bpass, 0, 0, 127)) * 8) + int(find(bpass, 7, 0, 7)))

print(max(ids))