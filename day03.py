with open("input/day03_input.txt", "r") as f:
    lines = f.readlines()

def perform_multiplications_part_1(line):
    i = 0
    n = len(line)
    sum_of_prods = 0
    
    while i < n:
        if line[i:i+4] == "mul(":
            j = i + 4
            first_arg = ""

            while j < n and line[j].isdigit():
                first_arg += line[j]
                j += 1

            # invalid arg1
            if j == i + 4 or line[j] != ",":
                i = j
                continue
 
            j += 1
            prev_j = j
            second_arg = ""
            
            while j < n and line[j].isdigit():
                second_arg += line[j]
                j += 1

            # invalid arg2
            if j == prev_j or line[j] != ")":
                i = j
                continue

            sum_of_prods += int(first_arg) * int(second_arg)
            i = j + 1
        else:
            i += 1

    return sum_of_prods

def perform_multiplications_part_2(line, multiplication_status):
    i = 0
    n = len(line)
    sum_of_prods = 0
    enable_multiplication = multiplication_status
    
    while i < n:
        if line[i:i+4] == "do()":
            enable_multiplication = True
            i += 4
        elif line[i:i+7] == "don't()":
            enable_multiplication = False
            i += 7
        elif line[i:i+4] == "mul(" and enable_multiplication:
            j = i + 4
            first_arg = ""

            while j < n and line[j].isdigit():
                first_arg += line[j]
                j += 1

            # invalid arg1
            if j == i + 4 or line[j] != ",":
                i = j
                continue
 
            j += 1
            prev_j = j
            second_arg = ""

            while j < n and line[j].isdigit():
                second_arg += line[j]
                j += 1

            # invalid arg2
            if j == prev_j or line[j] != ")":
                i = j
                continue

            sum_of_prods += int(first_arg) * int(second_arg)
            i = j + 1
        else:
            i += 1

    return (sum_of_prods, enable_multiplication)

ans1 = 0
ans2 = 0
multiplication_status = True
for line in lines:
    ans1 += perform_multiplications_part_1(line)
    line_sum, multiplication_status = perform_multiplications_part_2(line, multiplication_status)
    ans2 += line_sum

print(ans1)
print(ans2)