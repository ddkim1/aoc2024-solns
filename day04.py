xmas = "XMAS"
p1_directions = [(-1,1),(1,1),(1,-1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
p2_directions = [(-1,1),(1,1),(1,-1),(-1,-1)]

with open("input/day04_input.txt", "r") as f:
    lines = f.readlines()

xmas_grid = []
for line in lines:
    letters = []
    for ch in line:
        if ch != '\n':
            letters.append(ch)

    xmas_grid.append(letters)

def out_of_bounds(row, col):
    return row < 0 or row >= len(xmas_grid) or col < 0 or col >= len(xmas_grid[0])

def find_xmas(row, col, dR, dC):
    for i in range(4):
        newR = row + dR * i
        newC = col + dC * i
        if out_of_bounds(newR, newC) or xmas_grid[newR][newC] != xmas[i]:
            return False
        
    return True


def find_xmas_cross(row, col):
    assert(xmas_grid[row][col] == 'A')

    num_M = 0
    num_S = 0
    for dR, dC in p2_directions:
        newR = row + dR
        newC = col + dC
        if out_of_bounds(newR, newC) or (xmas_grid[newR][newC] != 'M' and xmas_grid[newR][newC] != 'S'):
            return 0
        
        num_M += (xmas_grid[newR][newC] == 'M')
        num_S += (xmas_grid[newR][newC] == 'S')

    # Consider the case:
    # M . S
    # . A .
    # S . M
    if xmas_grid[row-1][col-1] == xmas_grid[row+1][col+1]:
        return 0

    return (num_M == num_S == 2)

ans1 = 0
ans2 = 0
for i in range(len(xmas_grid)):
    for j in range(len(xmas_grid[0])):
        if xmas_grid[i][j] == 'X':
            for dR, dC in p1_directions:
                ans1 += find_xmas(i, j, dR, dC)
        elif xmas_grid[i][j] == 'A':
            ans2 += find_xmas_cross(i, j)

print(ans1)
print(ans2)