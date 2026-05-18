import heapq
import copy

# Goal State
goal = [['A', 'D', 'B'],
        ['E', 'F', 'C'],
        []]


# Generate next states
def next_states(state):

    states = []

    for i in range(3):

        if state[i]:

            for j in range(3):

                if i != j:

                    new = copy.deepcopy(state)

                    block = new[i].pop()

                    new[j].append(block)

                    states.append(new)

    return states


# Heuristic 1 - Misplaced Blocks
def h1(state):

    count = 0

    for i in range(3):

        for j in range(min(len(state[i]), len(goal[i]))):

            if state[i][j] != goal[i][j]:
                count += 1

    return count


# Heuristic 2 - Wrong Stacks
def h2(state):

    count = 0

    for i in range(3):

        if state[i] != goal[i]:
            count += 1

    return count


# Heuristic 3 - Stack Size Difference
def h3(state):

    return sum(abs(len(state[i]) - len(goal[i])) for i in range(3))


# Best First Search
def best_first(start, heuristic):

    pq = [(heuristic(start), start, 0)]

    visited = []

    while pq:

        h, state, steps = heapq.heappop(pq)

        if state == goal:
            return steps

        if state in visited:
            continue

        visited.append(state)

        for nxt in next_states(state):

            heapq.heappush(
                pq,
                (heuristic(nxt), nxt, steps + 1)
            )

    return -1


# Initial State
start = [['E'],
         ['B', 'F'],
         ['D', 'A', 'C']]


# Print Initial State
print("Initial State:\n")

for stack in start:
    print(*stack)

# Print Goal State
print("\nGoal State:\n")

for stack in goal:
    print(*stack)


# Run all heuristics
heuristics = [("h1", h1), ("h2", h2), ("h3", h3)]

for name, h in heuristics:

    print("\n-------------------------")
    print("Heuristic :", name)
    print("Steps Needed :", best_first(start, h))
    print("-------------------------")
