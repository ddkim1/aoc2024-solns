with open("input/day7_input.txt", "r") as f:
    lines = f.readlines()

def is_solvable_1(target, nums, curr):
    if len(nums) == 0:
        return (curr == target)
    
    return is_solvable_1(target, nums[1:], curr + nums[0]) or is_solvable_1(target, nums[1:], curr * nums[0])

def is_solvable_2(target, nums, curr):
    if len(nums) == 0:
        return (curr == target)
    
    return is_solvable_2(target, nums[1:], curr + nums[0]) or is_solvable_2(target, nums[1:], curr * nums[0]) or is_solvable_2(target, nums[1:], curr * (10 ** (len(str(nums[0])))) + nums[0])

ans1 = 0
ans2 = 0
for line in lines:
    target, rest = line.split(":")
    target = int(target)
    nums = list(map(int, rest.strip().split()))
    if is_solvable_1(target, nums[1:], nums[0]):
        ans1 += target
    if is_solvable_2(target, nums[1:], nums[0]):
        ans2 += target

print(ans1)
print(ans2)