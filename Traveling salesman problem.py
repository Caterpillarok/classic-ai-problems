import random


# Find total travelling cost
def cost(path, dist):

    total = 0

    for i in range(len(path) - 1):

        total += dist[path[i]][path[i + 1]]

    # Return to starting city
    total += dist[path[-1]][path[0]]

    return total


# Generate neighboring paths
def neighbors(path):

    all_neighbors = []

    for i in range(len(path)):

        for j in range(i + 1, len(path)):

            new_path = path[:]

            # Swap two cities
            new_path[i], new_path[j] = new_path[j], new_path[i]

            all_neighbors.append(new_path)

    return all_neighbors


# Number of cities
n = 5


# Create random distance matrix
dist = []

for i in range(n):

    row = []

    for j in range(n):

        if i == j:
            row.append(0)

        else:
            row.append(random.randint(1, 10))

    dist.append(row)


# Create random initial path
current = list(range(n))

random.shuffle(current)


# Hill Climbing
while True:

    best = current

    best_cost = cost(current, dist)

    # Check all neighboring paths
    for path in neighbors(current):

        new_cost = cost(path, dist)

        # Store better path
        if new_cost < best_cost:

            best = path

            best_cost = new_cost

    # Stop if no better path found
    if best == current:
        break

    # Move to better path
    current = best


# Output
print("Travelling Salesman Problem - Hill Climbing")

print("Distance Matrix:")

for row in dist:
    print(row)

print("Best Path:", current)

print("Minimum Cost:", cost(current, dist))
