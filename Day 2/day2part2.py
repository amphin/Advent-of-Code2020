with open("C:/Users/abies/Documents/Advent of Code/Day 2/day2input.txt") as file:
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
