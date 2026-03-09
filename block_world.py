import heapq

# ---------------- GOAL ----------------
goal = (("A","D","B"), ("E","F","C"), ())

# Precompute goal positions (for better heuristic)
goal_pos = {}
for i in range(3):
    for j in range(len(goal[i])):
        goal_pos[goal[i][j]] = (i, j)

# ---------------- SUCCESSORS ----------------
def successors(state):
    result = []
    for i in range(3):
        if not state[i]:
            continue
        for j in range(3):
            if i == j:
                continue

            new = [list(s) for s in state]
            block = new[i].pop()
            new[j].append(block)
            result.append(tuple(tuple(s) for s in new))
    return result

# ---------------- HEURISTIC 1 ----------------
# Count misplaced blocks (position-wise)
def h1(state):
    return sum(
        state[i][j] != goal[i][j]
        for i in range(3)
        for j in range(min(len(state[i]), len(goal[i])))
    )

# ---------------- HEURISTIC 2 ----------------
# Count blocks in wrong stack
def h2(state):
    count = 0
    for i in range(3):
        for block in state[i]:
            if goal_pos[block][0] != i:
                count += 1
    return count

# ---------------- HEURISTIC 3 ----------------
# Manhattan distance (stack + height difference)
def h3(state):
    dist = 0
    for i in range(3):
        for j in range(len(state[i])):
            gi, gj = goal_pos[state[i][j]]
            dist += abs(i - gi) + abs(j - gj)
    return dist

# ---------------- BEST FIRST SEARCH ----------------
def best_first(start, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic(start), start))

    visited = set()
    parent = {}
    nodes = 0

    while pq:
        _, state = heapq.heappop(pq)
        nodes += 1

        if state == goal:
            # Calculate path length
            length = 0
            temp = state
            while temp in parent:
                temp = parent[temp]
                length += 1
            return length, nodes

        if state in visited:
            continue
        visited.add(state)

        for nxt in successors(state):
            if nxt not in visited:
                parent[nxt] = state
                heapq.heappush(pq, (heuristic(nxt), nxt))

    return None, nodes

# ---------------- RUN ----------------
start = (("E",), ("B","F"), ("D","A","C"))

for h in [h1, h2, h3]:
    length, nodes = best_first(start, h)
    print(f"{h.__name__} -> Path Length: {length}, Nodes Expanded: {nodes}")
