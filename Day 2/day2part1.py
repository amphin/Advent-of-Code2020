with open("C:/Users/abies/Documents/Advent of Code/Day 2/day2input.txt") as file:
    passwords = file.read().splitlines()

valid = 0

for i in passwords:
    split_line = i.split()

    min_count = int(split_line[0].split('-')[0])
    max_count = int(split_line[0].split('-')[1])
    character = split_line[1].strip(':')
    password = split_line[2]

    char_count = 0
    for j in range(0, len(password)):
        if password[j] == character:
            char_count += 1
    
    if char_count >= min_count and char_count <= max_count:
        valid += 1

print(valid)
