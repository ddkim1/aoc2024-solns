def isSafe1(line):
    n = len(line)
    isIncreasing = 1
    isDecreasing = 1
    isWithinBounds = 1

    for i in range(n-1):
        curr, nxt = int(line[i]), int(line[i+1])
        diff = abs(nxt - curr)
        
        isIncreasing = isIncreasing and (curr < nxt)
        isDecreasing = isDecreasing and (curr > nxt)
        isWithinBounds = isWithinBounds and (diff <= 3 and diff >= 1)

    return (isIncreasing or isDecreasing) and isWithinBounds

def isSafe1Removed(line):
    n = len(line)

    for i in range(n):
        removed_i = line[:i] + line[i+1:]
        if isSafe1(removed_i):
            return 1
        
    return 0

def isSafe2(line):
    return isSafe1(line) or isSafe1Removed(line)

with open("input/day2_input.txt", "r") as f:
    lines = f.readlines()

ans1 = 0
ans2 = 0
for line in lines:
    ans1 += isSafe1(line.split())
    ans2 += isSafe2(line.split())

print(ans1)
print(ans2)