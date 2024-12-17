from collections import defaultdict, deque
import math

with open("input/day14_input.txt", "r") as f:
    lines = f.readlines()

positions = []
velocities = []

for line in lines:
    p_string, v_string = line.split(" ")
    p_coords = p_string.split("=")[1].split(",")
    p_x, p_y = int(p_coords[0]), int(p_coords[1])
    v_coords = v_string.split("=")[1].split(",")
    v_x, v_y = int(v_coords[0]), int(v_coords[1])
    positions.append((p_x, p_y))
    velocities.append((v_x, v_y))

rows = 103
cols = 101
mid_row = (rows - 1) // 2
mid_col = (cols - 1) // 2

NUM_ITERATIONS = 100

q1, q2, q3, q4 = 0, 0, 0, 0
for i in range(len(positions)):
    p_x, p_y = positions[i]
    v_x, v_y = velocities[i]

    new_x, new_y = p_x + v_x * NUM_ITERATIONS, p_y + v_y * NUM_ITERATIONS
    new_x %= cols
    new_y %= rows
    
    '''
    using the following quadrant scheme:

    q1 | q2
    -------
    q3 | q4
    '''

    if (new_x == mid_col or new_y == mid_row):
        continue

    if (new_x < mid_col and new_y < mid_row):
        q1 += 1

    elif (new_x > mid_col and new_y < mid_row):
        q2 += 1

    elif (new_x > mid_col and new_y > mid_row):
        q3 += 1

    else:
        q4 += 1

ans1 = q1 * q2 * q3 * q4
print(ans1)

# if the robots are in a tree, likely we have a decent number of robots
# that are contiguous in a row
# let's set the number that need to be in a row to 20, and we probably have a tree.
NUM_CLOSE_FOR_TREE = 20
def detect_close(positions):
    for row in range(rows):
        num_close = 0
        robots_in_row = [pos[0] for pos in positions if pos[1] == row]
        robots_in_row.sort()
        for i in range(1, len(robots_in_row)):
            if robots_in_row[i] == robots_in_row[i-1] + 1:
                num_close += 1

            if num_close >= NUM_CLOSE_FOR_TREE:
                return True

    return False

num_seconds = 1
while True:
    for i in range(len(positions)):
        p_x, p_y = positions[i]
        v_x, v_y = velocities[i]

        new_x, new_y = p_x + v_x, p_y + v_y
        new_x %= cols
        new_y %= rows

        positions[i] = new_x, new_y
        
    if detect_close(positions[:]):
        break
    
    num_seconds += 1

grid = [[0] * cols for _ in range(rows)]

# robots are *, empty is .
def draw_robots():
    # clear grid
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = "."

    # fill grid with robot locations
    for i in range(len(positions)):
        p_x, p_y = positions[i]
        grid[p_y][p_x] = "*"

    # display robots
    for i in range(rows):
        print("".join(grid[i]))
        print("\n")

ans2 = num_seconds
print(ans2)
draw_robots()