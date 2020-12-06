import os, sys

answers = []
gline = []
index = 0

with open(os.path.join(sys.path[0], "day6input.txt")) as file:
    for line in file.read().splitlines():
        if line == '':
            answers.append(gline)
            gline = []
            index += 1
        else:
            gline.append(line)
    answers.append(gline)

gcount = 0  
for group in answers:
    letters = {}
    for answer in group:
        for char in answer:
            if char not in letters:
                letters[char] = 1
            else:
                count = letters[char]
                letters[char] = count + 1
    for char in letters:
        if letters[char] == len(group):
            gcount += 1

print(gcount)