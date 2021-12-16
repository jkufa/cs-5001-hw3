# start at random location
# look at all directions around a cell, compute nextsum for each direction
# a valid cell is a reachable cell (blank cell)

from random import choice

DIMENSIONS = [6,8]
GAMMA = 0.8  # Discount rate
N = 10  # Number of iterations
INF = 9999999

# Mapping of all rewards
REWARDS = {
  (1, 3): 3, #🍩
  (1, 6): -10, #👹
  (3, 3): -5, #🔥
  (3, 6): 10 #🍰
}

# Dictionary of all possible actions
ACTIONS = {
  (1, 1): ("v"),
  (1, 4): (">"),
  (1, 5): ("v", "<"),
  (2, 1): ("^", "v", ">"),
  (2, 2): ("<", ">"),
  (2, 3): ("<"),
  (2, 5): ("^", "v"),
  (3, 1): ("^", "v"),
  (3, 5): ("^", "v"),
  (4, 1): ("^", ">"),
  (4, 2): ("<", ">"),
  (4, 3): ("<", ">"),
  (4, 4): ("<", ">"),
  (4, 5): ("^", "<"),
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
    else:
      V[s] = -1
    if s in REWARDS.keys():
        V[s] = REWARDS[s]

R = V

#Define initial policy
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

# TODO: finish exp_reward and prob functions, make sure v_next and v_prev are being set properly!
def value_iteration():
    for i in range(N):
        for s in ALL_STATES:
            if s in POLICY:
                new_v = 0

                for a in ACTIONS[s]:
                    nxt_sum = 0
                    alt_a1 = s
                    alt_a2 = s
                    if a == "^":
                        nxt = (s[0]-1, s[1])
                        if "<" in ACTIONS[s]:
                          alt_a1 = (s[0], s[1]-1) # L
                        if ">" in ACTIONS[s]:
                          alt_a2 = (s[0], s[1]+1) # R
                    if a == "v":
                        nxt = (s[0]+1, s[1])
                        # if "<" in ACTIONS[s]:
                        alt_a1 = (s[0], s[1]-1) # L
                        # if ">" in ACTIONS[s]:
                        alt_a2 = (s[0], s[1]+1) # R
                    if a == "<":
                        nxt = (s[0], s[1]-1)
                        # if "v"in ACTIONS[s]:
                        alt_a1 = (s[0]+1, s[1]) # L
                        # if "^" in ACTIONS[s]:
                        alt_a2 = (s[0]-1, s[1]) # R
                    if a == ">":
                        nxt = (s[0], s[1]+1)
                        # if "v"in ACTIONS[s]:
                        alt_a1 = (s[0]+1, s[1]) # L
                        # if "^" in ACTIONS[s]:
                        alt_a2 = (s[0]-1, s[1]) # R
                    nxt_sum = (.82 * V[nxt]) + (.09 * V[alt_a1]) + (.09 * V[alt_a2])
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
        actions.append(POLICY[s]+ "  ")
  print('CS-5001: HW#3\nProgrammer: Jack Kufa\nDiscount Gamma = ' + str(GAMMA)+'\n\nValues after ' + str(N) + ' iterations:\n'+r)
  for i in range(4):
    line = "|"
    for j in range(6):
      entry = values[0].rjust(6, ' ')
      line += " " + entry + " |"
      values.pop(0)
    print(line)
    print(r)

  print('\nPolicy:\n'+r)
  for i in range(4):
    line = "|"
    for j in range(6):
      entry = actions[0].rjust(6, ' ')
      line += " " + entry + " |"
      actions.pop(0)
    print(line+'\n'+r)




def output_policy():
  pass

value_iteration()
print_output()
# print(V)

# for rc in POLICY.keys():
#   print(rc, POLICY[rc])