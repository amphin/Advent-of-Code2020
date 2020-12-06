import os, sys

answers = []
gline = ""
index = 0

with open(os.path.join(sys.path[0], "day6input.txt")) as file:
    for line in file.read().splitlines():
        if line == '':
            answers.append(gline)
            gline = ""
            index += 1
        else:
            gline += gline + line
    answers.append(gline)
    
lcount = 0
for answer in answers:
    letters = []
    for char in answer:
        if char not in letters:
            letters.append(char)
    lcount += len(letters)

print(lcount)