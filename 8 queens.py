import random
import math


def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i+3])

    print()


def heuristic(state, goal):

    count = 0

    for i in range(9):

        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


def neighbors(state):

    result = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in moves:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            new = state[:]

            new_blank = nr * 3 + nc

            new[blank], new[new_blank] = \
                new[new_blank], new[blank]

            result.append(new)

    return result


def simulated_annealing(initial, goal):

    current = initial

    T = 100

    while T > 1:

        print_puzzle(current)

        if current == goal:
            print("Goal Reached!")
            return

        next_state = random.choice(neighbors(current))

        current_h = heuristic(current, goal)
        next_h = heuristic(next_state, goal)

        delta = next_h - current_h

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = next_state

        T *= 0.95

    print("Solution Not Found")


initial = [
    1, 2, 3,
    4, 0, 5,
    7, 8, 6
]

goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

simulated_annealing(initial, goal)
