from collections import defaultdict, deque

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

directions = [(-1,0), (0,1), (1,0), (0,-1)]

with open("input/day6_input.txt", "r") as f:
    lines = f.readlines()

grid_map = []
starting = []
for i in range(len(lines)):
    line = lines[i]
    if '^' in line:
        starting.append(i)
        starting.append(line.find('^'))

    grid_map.append(list(line.strip()))

def in_bounds(x, y):
    return (0 <= x and x < len(grid_map) and 0 <= y and y < len(grid_map[0]))

def move(x, y, dir, visited):
    while True:
        visited.add((x,y,dir))
        dX, dY = directions[dir]
        newX, newY = x + dX, y + dY

        if (newX, newY, dir) in visited:
            return 0

        if not in_bounds(newX, newY):
            break

        if grid_map[newX][newY] == '#':
            dir = (dir + 1) % 4
        else:
            x, y = newX, newY

    return len(visited)

ans1 = move(starting[0], starting[1], NORTH, set())
ans2 = 0

for i in range(len(grid_map)):
    for j in range(len(grid_map[0])):
        if grid_map[i][j] == '.':
            grid_map[i][j] = '#'

            if (move(starting[0], starting[1], NORTH, set()) == 0):
                ans2 += 1
                
            grid_map[i][j] = '.'

print(ans1)
print(ans2)