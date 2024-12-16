from collections import defaultdict, deque
import math

with open("input/day09_input.txt", "r") as f:
    lines = f.readlines()

line = lines[0].rstrip()

line_list = []
id = 0
block_map = dict()
free_blocks = []
for i in range(len(line)):
    num = int(line[i])
    append_val = None
    if i % 2:
        append_val = '.'
        free_blocks.append((len(line_list), num))
    else:
        append_val = id
        id += 1

    while num:
        line_list.append(append_val)
        num -= 1

def p1(line_list):
    i = 0
    j = len(line_list) - 1

    while i < j:
        while line_list[i] != '.':
            i += 1

        while line_list[j] == '.':
            j -= 1

        if i >= j:
            break

        line_list[i] = line_list[j]
        line_list[j] = '.'
        line_list.pop(j)
        i += 1
        j -= 1

    ans = 0
    i = 0
    while line_list[i] != '.':
        ans += i * line_list[i]
        i += 1

    return ans

def p2(line_list):
    i = len(line_list) - 1
    while i:
        # find next non free block
        while i and line_list[i] == '.':
            i -= 1

        if not i:
            break

        block_len = 0
        id = line_list[i]
        while i and line_list[i] == id:
            block_len += 1
            i -= 1

        # find free block to place block into
        j = 0
        while j < len(free_blocks):
            curr_idx, curr_len = free_blocks[j]

            # no free block left of block
            if curr_idx > i:
                break

            # found free block that fits block
            if curr_len >= block_len:
                k = curr_idx
                l = i + 1
                while block_len:
                    line_list[k] = id
                    line_list[l] = '.'
                    k += 1
                    l += 1
                    block_len -= 1
                    curr_len -= 1

                # update entry
                if curr_len == 0:
                    free_blocks.pop(j)
                else:
                    free_blocks[j] = (k, curr_len)

                break

            j += 1

    ans = 0
    i = 0
    while i < len(line_list):
        if line_list[i] != '.':
            ans += i * line_list[i]
        i += 1

    return ans

ans1 = p1(line_list[:])
ans2 = p2(line_list[:])
print(ans1)
print(ans2)