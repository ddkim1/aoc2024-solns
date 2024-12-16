from collections import defaultdict, deque
import math

with open("input/day08_input.txt", "r") as f:
    lines = f.readlines()

antennas = defaultdict(list)
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            antennas[lines[i][j]].append((i, j))

def in_bounds(i, j):
    return (0 <= i and i < len(lines) and 0 <= j and j < len(lines[0]))

def num_antinodes_pt1():
    antinodes = set()
    for antenna in antennas.keys():
        all_locations = antennas[antenna]
        for i in range(len(all_locations)):
            for j in range(len(all_locations)):
                if i == j:
                    continue

                ix, iy = all_locations[i]
                jx, jy = all_locations[j]
                dx, dy = (jx - ix), (jy - iy)
                ax, ay = (jx + dx), (jy + dy)

                if in_bounds(ax, ay):
                    antinodes.add((ax, ay))

    return len(antinodes)

def num_antinodes_pt2():
    antinodes = set()
    for antenna in antennas.keys():
        all_locations = antennas[antenna]
        for i in range(len(all_locations)):
            for j in range(len(all_locations)):
                if i == j:
                    continue

                ix, iy = all_locations[i]
                jx, jy = all_locations[j]
                dx, dy = (jx - ix), (jy - iy)
                dx, dy = dx / math.gcd(dx, dy), dy / math.gcd(dx, dy)
                ax, ay = ix, iy

                while in_bounds(ax, ay):
                    antinodes.add((ax, ay))
                    ax += dx
                    ay += dy

    return len(antinodes)

ans1 = num_antinodes_pt1()
ans2 = num_antinodes_pt2()
print(ans1)
print(ans2)