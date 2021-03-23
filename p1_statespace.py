import copy
def fill(state, max, which):
    # use deepcopy to save the state
    s0 = copy.deepcopy(state)
    if which == 0:
        s0[0] = max[0]
    if which == 1:
        s0[1] = max[1]
    return s0

def empty(state, max, which):
    # use deepcopy to save the state
    s0 = copy.deepcopy(state)
    if which == 0:
        s0[0] = 0
    if which == 1:
        s0[1] = 0
    return s0

def xfer(state, max, source, dest):
    # use deepcopy to save the state
    s0 = copy.deepcopy(state)

    if s0[source] >= max[dest] - s0[dest]:
        s0[dest] = max[dest]
        s0[source] = s0[source] - (max[dest] - s0[dest])
    elif s0[source] < max[dest] - s0[dest]:
        s0[dest] = s0[source] + s0[dest]
        s0[source] = 0
    return s0

def succ(state, max):
    # to remove duplication
    s1 = empty(state, max, 0)
    s2 = empty(state, max, 1)
    if s1 == s2:
        print(s1)
    else:
        print(s1)
        print(s2)

    # to remove duplication
    s3 = fill(state, max, 0)
    s4 = fill(state, max, 1)
    if s3 == s4:
        print(s3)
    else:
        print(s3)
        print(s4)

    if state[0] != 0 & state[1] != max[1]:
        print(xfer(state,max,0,1))
    if state[1] != 0 & state[0] != max[0]:
        print(xfer(state,max,1,0))


