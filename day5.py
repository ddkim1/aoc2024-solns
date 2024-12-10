from collections import defaultdict, deque

with open("input/day5_input.txt", "r") as f:
    lines = f.readlines()

page_graph = defaultdict(set)
for i in range(len(lines)):
    if lines[i] == "\n":
        break

    pages = lines[i].split("|")
    page_graph[int(pages[0])].add(int(pages[1][:-1]))

def dfs(pages, visited):
    if len(pages) == 1:
        return True
    
    for page_child in page_graph[pages[0]]:
        if pages[1] == page_child:
            if page_child not in visited:
                visited.add(page_child)
                if dfs(pages[1:], visited):
                    return True
            else:
                return False

    return False

def topo_sort(page_order):
    page_order_set = set(page_order)
    contained_dag = defaultdict(set)
    incoming_edges = defaultdict(int)

    for i in range(len(lines)):
        if lines[i] == "\n":
            break

        pages = lines[i].split("|")
        if int(pages[0]) not in page_order_set or int(pages[1][:-1]) not in page_order_set:
            continue

        contained_dag[int(pages[0])].add(int(pages[1][:-1]))
        incoming_edges[int(pages[1][:-1])] += 1

    no_incoming_edges = deque([node for node in page_order_set if incoming_edges[node] == 0])
    correct_order = []

    while no_incoming_edges:
        curr_node = no_incoming_edges.popleft()
        correct_order.append(curr_node)
        for neighbor in contained_dag[curr_node]:
            incoming_edges[neighbor] -= 1
            if incoming_edges[neighbor] == 0:
                no_incoming_edges.append(neighbor)

    return correct_order

ans1 = 0
ans2 = 0
for j in range(i+1, len(lines)):
    page_order = list(map(int, lines[j].split(",")))
    if dfs(page_order, set()):
        ans1 += page_order[len(page_order) // 2]
    else:
        correct_order = topo_sort(page_order)
        ans2 += correct_order[len(correct_order) // 2]

print(ans1)
print(ans2)