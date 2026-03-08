import heapq


def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True


def heuristic(m_left, c_left):
    return m_left + c_left


def a_star_missionaries_cannibals():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    pq = []  # priority queue
    visited = set()

    # (f, g, state, path)
    heapq.heappush(pq, (heuristic(3, 3), 0, start, [start]))

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while pq:
        f, g, (m_left, c_left, boat), path = heapq.heappop(pq)

        if (m_left, c_left, boat) in visited:
            continue

        visited.add((m_left, c_left, boat))

        if (m_left, c_left, boat) == goal:
            print("\n✅ Goal Reached Using A*!\n")
            print(f"Total cost (g): {g}\n")
            for i, state in enumerate(path):
                print(f"Step {i}: {state}")
            return

        for m_move, c_move in moves:

            if boat == 1:
                new_state = (
                    m_left - m_move,
                    c_left - c_move,
                    0
                )
            else:
                new_state = (
                    m_left + m_move,
                    c_left + c_move,
                    1
                )

            new_m_left, new_c_left, new_boat = new_state

            if is_valid(new_m_left, new_c_left):

                new_g = g + 1
                new_h = heuristic(new_m_left, new_c_left)
                new_f = new_g + new_h

                if new_state not in visited:
                    heapq.heappush(
                        pq,
                        (new_f, new_g, new_state, path + [new_state])
                    )

    print("No solution found")


a_star_missionaries_cannibals()
