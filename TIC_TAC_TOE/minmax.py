import copy
BOARDLEN = 9

# returns all the successors (with action) given a state -- [action, successor]
def successors(state, turn):
    successors = []
    for i in range(BOARDLEN):
        if state[i] == -1:
            successor = [i, copy.deepcopy(state)]
            successor[1][i] = 0 if turn == "O" else 1
            successors.append(successor)
    return successors

# returns the current value of the game state
def utility(state, choice):
    result = checkState(state)
    if result == "draw":
        return 0
    if result == 1:
        return 1 if choice == "O" else -1
    if result == 0:
        return 1 if choice == "X" else -1

# checks the current state of the game
# if X won, return 1. If O won, return 0
def checkState(state):
    if state[0] == state[1] == state[2] and state[0] != -1:
        return state[0]
    if state[3] == state[4] == state[5] and state[3] != -1:
        return state[3]
    if state[6] == state[7] == state[8] and state[6] != -1:
        return state[6]
    if state[0] == state[3] == state[6] and state[0] != -1:
        return state[0]
    if state[1] == state[4] == state[7] and state[1] != -1:
        return state[1]
    if state[2] == state[5] == state[8] and state[2] != -1:
        return state[2]
    if state[0] == state[4] == state[8] and state[0] != -1:
        return state[0]
    if state[2] == state[4] == state[6] and state[2] != -1:
        return state[2]

    if -1 not in state:
        return "draw"
    else:
        return "not finished"

# Basically the base case for the minmax algorithm
def value(state, turn, choice):
    if -1 not in state or not isinstance(checkState(state), str): # if board is already full or someone already won
        return [-1, utility(state, choice)] # -1 is just a place holder, can be anything
    if turn != choice: # maximize the AI's, not the choice of the player
        return maxValue(state, turn, choice)
    else:
        return minValue(state, turn, choice)

# maximizes the value of a node. returns an array containing the action and its value
def maxValue(state, turn, choice):
    m = float("-inf")
    action = -1
    for successor in successors(state, turn):
        val = value(successor[1], "X" if turn == "O" else "O", choice)
        v = val[1]
        if v > m:
            m = v
            action = successor[0]

    return [action, m]

# minimizes the value of a node. returns an array containing the action and its value
def minValue(state, turn, choice):
    m = float("inf")
    action = -1
    for successor in successors(state, turn):
        val = value(successor[1], "X" if turn == "O" else "O", choice)
        v = val[1]
        if v < m:
            m = v
            action = successor[0]
    return [action, m]