# Value Iteration (Homework 3)
# Jack Kufa Fall 2021

from random import choice
from copy import deepcopy

GAMMA = 0.8  # Discount rate
N = 100000  # Number of iterations
INF = 9999999

# Mapping of all rewards
REWARDS = {
    (1, 3): 3, # 🍩 
    (1, 6): -10,  # 👹  
    (3, 3): -5, # 🔥  
    (3, 6): 10}  # 🍰

# Dictionary of all possible actions
ACTIONS = {
    (1, 1): ("v"),
    (1, 4): ("<", ">"),
    (1, 5): ("v", "<", ">"),
    (2, 1): ("^", "v", ">"),
    (2, 2): ("<", ">"),
    (2, 3): ("^", "v", "<"),
    (2, 5): ("^", "v"),
    (3, 1): ("^", "v"),
    (3, 5): ("^", "v", ">"),
    (4, 1): ("^", ">"),
    (4, 2): ("<", ">"),
    (4, 3): ("^", "<", ">"),
    (4, 4): ("<", ">"),
    (4, 5): ("^", "<"),
}

# Define all states
ALL_STATES = []
for i in range(6):
    for j in range(8):
        ALL_STATES.append((i, j))

# Initialize V
V = {}
for s in ALL_STATES:
    if s in ACTIONS.keys():
        V[s] = 0
    else:
        V[s] = -1
    if s in REWARDS.keys():
        V[s] = REWARDS[s]

R = deepcopy(V)  # original state, contains original values of all the rewards

# Define initial policy
POLICY = {}
for s in ACTIONS.keys():
    POLICY[s] = choice(ACTIONS[s])


def get_locations(a, s):
    if a == "^":
        # up left right
        return (s[0] - 1, s[1]), (s[0], s[1] - 1), (s[0], s[1] + 1)
    elif a == "v":
        # down left right
        return (s[0] + 1, s[1]), (s[0], s[1] - 1), (s[0], s[1] + 1)
    elif a == "<":
        # left up down
        return (s[0], s[1] - 1), (s[0] - 1, s[1]), (s[0] + 1, s[1])
    elif a == ">":
        # right up down
        return (s[0], s[1] + 1), (s[0] - 1, s[1]), (s[0] + 1, s[1])


def value_iteration():
    for i in range(N):
        for s in ALL_STATES:
            if s in POLICY:
                new_v = -INF

                for a in ACTIONS[s]:
                    nxt, alt_a1, alt_a2 = get_locations(a, s)
                    # perform probability calculations
                    nxt_sum = (0.82 * V[nxt]) + (0.09 * V[alt_a1]) + (0.09 * V[alt_a2])
                    v = R[s] + GAMMA * nxt_sum

                    if v > new_v:
                        new_v = v
                        POLICY[s] = a
                V[s] = new_v


def print_output():
    r = "+--------+--------+--------+--------+--------+--------+"
    values = []
    actions = []
    for s in V:
        if s[0] != 0 and s[0] != 5 and s[1] != 0 and s[1] != 7:
            if V[s] == -1:
                values.append("XXXXXX")
                actions.append("XXXXXX")
            elif V[s] == 10:
                values.append("CAKE")
                actions.append("CAKE")
            elif V[s] == 3:
                values.append("DONUT")
                actions.append("DONUT")
            elif V[s] == -5:
                values.append("FIRE")
                actions.append("FIRE")
            elif V[s] == -10:
                values.append("ONI")
                actions.append("ONI")
            else:
                values.append(str(V[s])[0:5])
                actions.append(POLICY[s] + "  ")
    print(
        "CS-5001: HW#3\nProgrammer: Jack Kufa\nDiscount Gamma = "
        + str(GAMMA)
        + "\n\nValues after "
        + str(N)
        + " iterations:\n"
        + r
    )
    for i in range(4):
        line = "|"
        for j in range(6):
            entry = values[0].rjust(6, " ")
            line += " " + entry + " |"
            values.pop(0)
        print(line)
        print(r)

    print("\nPolicy:\n" + r)
    for i in range(4):
        line = "|"
        for j in range(6):
            entry = actions[0].rjust(6, " ")
            line += " " + entry + " |"
            actions.pop(0)
        print(line + "\n" + r)


if __name__ == "__main__":
    value_iteration()
    print_output()
