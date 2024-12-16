from collections import defaultdict, deque
import math

with open("input/day12_input.txt", "r") as f:
    lines = f.readlines()

grid = []

for line in lines:
    line = line.rstrip()
    row = []
    for ch in line:
        row.append(ch)

    grid.append(row)

def calculate_region(i, j):
    area = 0
    perimeter = 0
    char = grid[i][j]
    queue = deque()
    queue.append((i, j))
    visited = set()
    visited.add((i, j))
    num_sides = 0

    while queue:
        row, col = queue.popleft()
        area += 1

        if ((row - 1, col) not in visited) and (row - 1) >= 0 and grid[row - 1][col] == char:
            visited.add((row-1, col))
            queue.append((row-1, col))

        if ((row, col - 1) not in visited) and (col - 1) >= 0 and grid[row][col - 1] == char:
            visited.add((row, col-1))
            queue.append((row, col-1))

        if ((row + 1, col) not in visited) and (row + 1) < len(grid) and grid[row + 1][col] == char:
            visited.add((row+1, col))
            queue.append((row+1, col))

        if ((row, col + 1) not in visited) and (col + 1) < len(grid[0]) and grid[row][col + 1] == char:
            visited.add((row, col+1))
            queue.append((row, col+1))

        if (row - 1) < 0 or grid[row - 1][col] != char:
            perimeter += 1

        if (col - 1) < 0 or grid[row][col - 1] != char:
            perimeter += 1

        if (row + 1) >= len(grid) or grid[row + 1][col] != char:
            perimeter += 1

        if (col + 1) >= len(grid[0]) or grid[row][col + 1] != char:
            perimeter += 1

        north = (row - 1 >= 0) and grid[row-1][col] == char
        south = (row + 1 < len(grid)) and grid[row+1][col] == char
        west = (col - 1 >= 0) and grid[row][col-1] == char
        east = (col + 1 < len(grid[0])) and grid[row][col+1] == char
        nw = (row - 1 >= 0 and col - 1 >= 0) and grid[row-1][col-1] == char
        ne = (row - 1 >= 0 and col + 1 < len(grid[0])) and grid[row-1][col+1] == char
        sw = (row + 1 < len(grid) and col - 1 >= 0) and grid[row+1][col-1] == char
        se = (row + 1 < len(grid) and col + 1 < len(grid[0])) and grid[row+1][col+1] == char

        corner_conditions = [not (north or west), not (north or east), not (south or west), not (south or east), north and west and not nw, north and east and not ne, south and west and not sw, south and east and not se]
        num_sides += sum(corner_conditions)
        
    return area, perimeter, num_sides

def clear_region(i, j):
    char = grid[i][j]
    queue = deque()
    queue.append((i, j))
    visited = set()
    visited.add((i, j))

    while queue:
        row, col = queue.popleft()
        grid[row][col] = -1

        if ((row - 1, col) not in visited) and (row - 1) >= 0 and grid[row - 1][col] == char:
            visited.add((row-1, col))
            queue.append((row-1, col))

        if ((row, col - 1) not in visited) and (col - 1) >= 0 and grid[row][col - 1] == char:
            visited.add((row, col-1))
            queue.append((row, col-1))

        if ((row + 1, col) not in visited) and (row + 1) < len(grid) and grid[row + 1][col] == char:
            visited.add((row+1, col))
            queue.append((row+1, col))

        if ((row, col + 1) not in visited) and (col + 1) < len(grid[0]) and grid[row][col + 1] == char:
            visited.add((row, col+1))
            queue.append((row, col+1))

ans1 = 0
ans2 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != -1:
            area, perimeter, sides = calculate_region(i, j)
            ans1 += area * perimeter
            ans2 += area * sides
            clear_region(i, j)

print(ans1)
print(ans2)