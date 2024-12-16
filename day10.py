from collections import defaultdict, deque
import math

with open("input/day10_input.txt", "r") as f:
    lines = f.readlines()

graph = []
for line in lines:
    line = line.rstrip()
    line_int = []
    for ch in line:
        line_int.append(int(ch))

    graph.append(line_int)

def bfs(i, j, unique):
    visited = set()
    visited.add((i, j))
    queue = deque()
    queue.append((i,j))
    ans = 0

    while queue:
        qLen = len(queue)
        for i in range(qLen):
            row, col = queue.popleft()

            if graph[row][col] == 9:
                ans += 1
                continue

            if ((row-1, col) not in visited) and (row-1) >= 0 and graph[row-1][col] == 1 + graph[row][col]:
                if unique:
                    visited.add((row-1, col))
                queue.append((row-1, col))

            if ((row, col-1) not in visited) and (col-1) >= 0 and graph[row][col-1] == 1 + graph[row][col]:
                if unique:
                    visited.add((row, col-1))
                queue.append((row, col-1))

            if ((row+1, col) not in visited) and (row+1) < len(graph) and graph[row+1][col] == 1 + graph[row][col]:
                if unique:
                    visited.add((row+1, col))
                queue.append((row+1, col))

            if ((row, col+1) not in visited) and (col+1) < len(graph[0]) and graph[row][col+1] == 1 + graph[row][col]:
                if unique:
                    visited.add((row, col+1))
                queue.append((row, col+1))

    return ans


ans1 = 0
ans2 = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 0:
            ans1 += bfs(i, j, True)
            ans2 += bfs(i, j, False)

print(ans1)
print(ans2)