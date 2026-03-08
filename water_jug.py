import math

#solvability based on GCD
def is_solvable(capacity1,capacity2,goal):
    if goal> max(capacity1,capacity2):
        return False
    if goal % math.gcd(capacity1,capacity2)!= 0:
        return False
    return True

def dfs():
    capacity1 = int(input("Enter the capacity of first jug: "))
    capacity2 = int(input("Enter the capacity of the second jug: "))
    goal = int(input("Enter the goal capacity: "))

    if not is_solvable(capacity1,capacity2,goal):
        print("\nNo solution possible(GCD)\n")
        return

    stack = []
    visited = set()
    
    stack.append(((0,0),[(0,0)]))

    while stack:
        (x,y),path = stack.pop()

        if(x,y) in visited:
            continue

        visited.add((x,y))

        if x == goal or y == goal:
            print("\nGoal reached\n")
            for elments in path:
                print(elments)
            return
        

        next_states = []
        #state generation

        next_states.append((capacity1,y))
        next_states.append((x,capacity2))
        next_states.append((0,y))
        next_states.append((x,0))

        #transfer from jug1->jug2
        transfer = min((x,capacity2-y))
        next_states.append((x-transfer,y+transfer))

        #transfer from jug2->jug1
        transfer = min(capacity1-x,y)
        next_states.append((x+transfer,y-transfer))


        for state in next_states:
            if state not in visited:
                stack.append((state,path + [state]))
                

    print("\nno solution found\n")
dfs()






        































