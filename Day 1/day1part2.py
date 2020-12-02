import os, sys

with open(os.path.join(sys.path[0], "day1input.txt")) as file:
    numbers = [int(n) for n in file]

numbers.sort()
for number1 in numbers:
    for number2 in numbers:
        for number3 in numbers:
            if (number1 + number2 + number3 == 2020):
                print(number1, "+", number2, "+", number3, "= 2020")
                print(number1, "x", number2, "x", number3, "=", str(number1*number2*number3))
                sys.exit()