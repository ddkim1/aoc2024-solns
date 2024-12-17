from collections import defaultdict, deque
import math

with open("input/day13_input.txt", "r") as f:
    lines = f.readlines()

def cramers(a1, a2, b1, b2, c1, c2):
    denom = a1 * b2 - b1 * a2
    x_num = (c1 * b2) - (b1 * c2)
    y_num = a1 * c2 - c1 * a2
    if ((x_num % denom) != 0 or (y_num % denom) != 0): 
        return -1, -1

    x = (c1 * b2 - b1 * c2) // (a1 * b2 - b1 * a2)
    y = (a1 * c2 - c1 * a2) // (a1 * b2 - b1 * a2)

    return x, y

def parse_button_line(line):
    add_info = line.split(":")[1]
    x_info, y_info = add_info.split(",")
    x_num = int(x_info.split("+")[1])
    y_num = int(y_info.split("+")[1])

    return x_num, y_num

def parse_prize_line(line):
    prize_info = line.split(":")[1]
    x_prize_info, y_prize_info = prize_info.split(",")
    x_prize_num = int(x_prize_info.split("=")[1])
    y_prize_num = int(y_prize_info.split("=")[1])

    return x_prize_num, y_prize_num


buttons = []
prizes = []
is_second_b_line = False
current_button = [0, 0, 0, 0]

for line in lines:
    if line == "\n":
        continue

    if line[0] == "B":
        x_num, y_num = parse_button_line(line)
        if not is_second_b_line:
            is_second_b_line = True
            current_button[0] = x_num
            current_button[1] = y_num
        else:
            is_second_b_line = False
            current_button[2] = x_num
            current_button[3] = y_num
            buttons.append(tuple(current_button))

    elif line[0] == "P":
        x_num, y_num = parse_prize_line(line)
        prizes.append((x_num, y_num))

P2_ADD = 10000000000000

def solve():
    num_tokens_p1 = 0
    num_tokens_p2 = 0
    for i in range(len(buttons)):
        a1, a2, b1, b2 = buttons[i]
        c1, c2 = prizes[i]

        a_tokens, b_tokens = cramers(a1, a2, b1, b2, c1, c2)
        if (a_tokens != -1 and b_tokens != -1):
            num_tokens_p1 += 3 * a_tokens + b_tokens

        a_tokens, b_tokens = cramers(a1, a2, b1, b2, c1 + P2_ADD, c2 + P2_ADD)
        if (a_tokens != -1 and b_tokens != -1):
            num_tokens_p2 += 3 * a_tokens + b_tokens

    return num_tokens_p1, num_tokens_p2

ans1, ans2 = solve()
print(ans1)
print(ans2)