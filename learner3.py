# start at random location
# look at all directions around a cell, compute nextsum for each direction
# a valid cell is a reachable cell (blank cell)

from random import choice

DIMENSIONS = [6,8]
GAMMA = 0.8  # Discount rate
N = 10000  # Number of iterations
INF = 9999999
# Mapping of all rewards
REWARDS = {
  (1, 3): -10, #👹
  (1, 6): 3, #🍩
  (3, 3): -5, #🔥
  (3, 6): 10 #🍰
}
# Dictionary of all possible actions
ACTIONS = {
  (1, 1): ("D"),
  (1, 4): ("R"),
  (1, 5): ("D", "L"),
  (2, 1): ("U", "D", "R"),
  (2, 2): ("L", "R"),
  (2, 3): ("L"),
  (2, 5): ("U", "D"),
  (3, 1): ("U", "D"),
  (3, 5): ("U", "D"),
  (4, 1): ("U", "R"),
  (4, 2): ("L", "R"),
  (4, 3): ("L", "R"),
  (4, 4): ("L", "R"),
  (4, 5): ("U", "L"),
}

#Define all states
ALL_STATES=[]
for i in range(6):
    for j in range(8):
            ALL_STATES.append((i,j))

# Initialize V
V={}
for s in ALL_STATES:
    if s in ACTIONS.keys():
        V[s] = 0
    if s in REWARDS.keys():
        V[s] = REWARDS[s]
    else:
      V[s] = -1

#Define an initial policy
POLICY={}
for s in ACTIONS.keys():
    POLICY[s] = choice(ACTIONS[s])


def prob(s, a, nxt):
    p = .09
    # determine if l_prime is the same direction as a and assign p to .82 if yes
    return p


def exp_reward(l, a):
    res = 0.0
    # foreach location reachable from l after action a
    # res += prob(l, a, l_prime) * reward(l, a, l_prime)
    return res


def reward(l_prime):
    res = REWARDS[MAZE[l_prime[0]][l_prime[1]]]
    return res


def value_iteration():

    for i in range(N):
        for s in ALL_STATES:
            v_next = -INF
            if s in POLICY:
                v_prev = V[s]

                for a in ACTIONS[s]:
                    nxt_sum = 0
                    if a == 'U':
                        nxt = (s[0]-1, s[1])
                    if a == 'D':
                        nxt = (s[0]+1, s[1])
                    if a == 'L':
                        nxt = (s[0], s[1]-1)
                    if a == 'R':
                        nxt = (s[0], s[1]+1)
                    nxt_sum += .82 * v_prev
                    v_tmp = exp_reward(s, a) + GAMMA * nxt_sum
                    if v_tmp > v_next:
                        v_next = v_tmp
                        POLICY[s] = a
                    V[s] = v_next

def optimal_policy():
    pass

value_iteration()
print(V)
print("/n/n")

for rc in POLICY.keys():
  print(rc, POLICY[rc])