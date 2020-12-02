import sys

with open("C:/Users/abies/Documents/Advent of Code/Day 1/day1input.txt") as file:
    numbers = [int(n) for n in file]

numbers.sort()
for number in numbers:
    for i in range(len(numbers)-1, -1, -1):
        if 2020 - number == numbers[i]:
            print(number, "+", numbers[i], "= 2020")
            print(number, "x", numbers[i], "=", str(number*numbers[i]))
            sys.exit()