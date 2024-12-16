from collections import defaultdict, deque
import math

with open("input/day11_input.txt", "r") as f:
    lines = f.readlines()

stones = list(map(int, lines[0].rstrip().split()))
stones_counter = defaultdict(int)

for stone in stones:
    stones_counter[stone] += 1

NUM_BLINKS1 = 25
NUM_BLINKS2 = 75

for i in range(NUM_BLINKS2):
    if i == NUM_BLINKS1:
        ans1 = sum(stones_counter.values())
    new_stones = defaultdict(int)
    for stone in stones_counter.keys():
        # stone is 0 -> turn into 1
        if stone == 0:
            new_stones[1] += stones_counter[stone]

        # stone is even len -> (left) (right)
        elif len(str(stone)) % 2 == 0:
            stone_list = list(str(stone))
            left_stone = stone_list[0:(len(stone_list) // 2)]
            right_stone = stone_list[(len(stone_list) // 2):]
            left_stone = int("".join(left_stone))
            right_stone = int("".join(right_stone))
            new_stones[left_stone] += stones_counter[stone]
            new_stones[right_stone] += stones_counter[stone]

        # stone -> stone * 2024
        else:
            new_stones[stone * 2024] += stones_counter[stone]

    stones_counter = new_stones

ans2 = sum(stones_counter.values())
print(ans1)
print(ans2)