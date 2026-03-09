SIZE = 4

percepts = {
    (1,1): {"B": False, "S": False, "G": False},
    (1,2): {"B": False, "S": True,  "G": False},
    (2,1): {"B": True,  "S": False, "G": False},
    (2,3): {"B": True,  "S": True,  "G": True }
}

def get_adj(x, y):
    return [(a,b) for a,b in
            [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            if 1 <= a <= SIZE and 1 <= b <= SIZE]


def logical_reasoning():
    safe = set(percepts)
    possible_pit = set()
    possible_wumpus = set()
    gold_location = None
    wumpus_location = None

    for (x, y), p in percepts.items():

        adj = get_adj(x, y)

        if p["G"]:
            gold_location = (x, y)

        for sense, danger_set in [("B", possible_pit),
                                  ("S", possible_wumpus)]:

            if not p[sense]:
                danger_set.difference_update(adj)
                safe.update(c for c in adj if c not in percepts)
            else:
                danger_set.update(c for c in adj if c not in percepts)

    if len(possible_wumpus) == 1:
        wumpus_location = next(iter(possible_wumpus))

    return safe, possible_pit, possible_wumpus, wumpus_location, gold_location


# ------------ MAIN ------------

print("=" * 45)
print("WUMPUS WORLD — LOGICAL REASONING")
print("=" * 45)

safe, pits, wumpus, w_loc, g_loc = logical_reasoning()

print("\nSafe Cells          :", sorted(safe))
print("Possible Pit Cells  :", sorted(pits))
print("Possible Wumpus     :", sorted(wumpus))
print("Wumpus Location     :", w_loc)
print("Gold Location       :", g_loc)

print("\n--- Agent Decision ---")
if g_loc:
    print("✅ Navigate to", g_loc, "to grab the Gold!")
if w_loc:
    print("⚠️ Shoot arrow toward", w_loc)
if pits:
    print("⚠️ Avoid", sorted(pits))
