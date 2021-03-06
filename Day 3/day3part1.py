import os, sys

with open(os.path.join(sys.path[0], "day3input.txt")) as file:
    forest = [[char for char in line] for line in file.read().splitlines()]

forest_x = len(forest[0]) - 1
forest_y = len(forest) - 1
pos_x = 0
pos_y = 0
tree_count = 0


while pos_y < forest_y:
    pos_x += 3
    pos_y += 1
    if pos_x > forest_x:
        pos_x -= forest_x + 1
    
    if forest[pos_y][pos_x] == '#':
        tree_count += 1

print(tree_count)
