from collections import defaultdict

a1 = []
a2 = []

with open("input/day1_input.txt", "r") as f:
    lines = f.readlines()
    a2_freq = defaultdict(int)

    for line in lines:
        nums = line.split()
        a1.append(int(nums[0]))
        a2.append(int(nums[1]))
        a2_freq[int(nums[1])] += 1
    
    a1.sort()
    a2.sort()
    
    n = len(a1)
    ans1 = 0
    ans2 = 0
    for i in range(n):
        ans1 += abs(a1[i] - a2[i])
        ans2 += a1[i] * a2_freq[a1[i]]
    
    print(ans1)
    print(ans2)