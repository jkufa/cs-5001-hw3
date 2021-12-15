REWARDS = {"🍰": 10, "🍩": 3, "🔥": -5, "👹": -10, "⬛": -1}

MAZE = [
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
    ["⬛", "", "⬛", "🍩", "", "", "👹", "⬛"],
    ["⬛", "", "", "", "⬛", "", "⬛", "⬛"],
    ["⬛", "", "⬛", "🔥", "⬛", "", "🍰", "⬛"],
    ["⬛", "", "", "", "", "", "⬛", "⬛"],
    ["⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛", "⬛"],
]

GAMMA = 0.8  # Discount rate
N = 10000  # iterations
v_next = []
v_prev = []


def prob(location, action, location2):
    pass


def exp_reward(location, action):
    pass


def reward(l1, a, l2):
    pass


def value_iteration():
    pass


def optimal_policy():
    pass
