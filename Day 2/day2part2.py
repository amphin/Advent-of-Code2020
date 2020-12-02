import os, sys

with open(os.path.join(sys.path[0], "day2input.txt")) as file:
    passwords = file.read().splitlines()

valid = 0

for i in passwords:
    split_line = i.split()

    pos1 = int(split_line[0].split('-')[0]) - 1
    pos2 = int(split_line[0].split('-')[1]) - 1
    character = split_line[1].strip(':')
    password = split_line[2]
    
    if (password[pos1] == character) != (password[pos2] == character):
        valid += 1

print(valid)
