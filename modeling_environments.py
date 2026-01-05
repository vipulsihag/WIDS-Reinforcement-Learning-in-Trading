import pprint

## Slippery Walk

swf_mdp = {}
actions = ["Left", "Right"]
swf_mdp[0] = {
    "Left": [(1.0, 0, 0, True)],
    "Right": [(1.0, 0, 0, True)]
}
swf_mdp[6] = {
    "Left": [(1.0, 6, 0, True)],
    "Right": [(1.0, 6, 0, True)]
}

for s in range(1,6):
    swf_mdp[s] = {}
    for a in actions:
        if a == "Right":
            wantTo = s + 1
            endUp = s - 1
        else:
            wantTo = s - 1
            endUp = s + 1

        transitions = []

        # wantTo move
        transitions.append((1/2, wantTo, 1 if wantTo == 6 else 0, True if wantTo in {0, 6} else False))
        # Stay
        transitions.append((1/3, s, 0, False))
        # endUp move
        transitions.append((1/6, endUp, 1 if endUp == 6 else 0, True if endUp in {0, 6} else False))
        swf_mdp[s][a] = transitions
print("\n\nSlippery Walk\n\n")
pprint.pprint(swf_mdp)

## Frozen Lake Env

def helper(action, x):
    if action == "Up":
        if x < 4 :
            return x
        else :
            return x-4
    elif action == "Down":
        if x>11 :
            return x
        else :
            return x+4
    elif action == "Left":
        if (x%4==0):
            return x
        else :
            return x-1
    elif action == "Right":
        if x%4 == 3:
            return x
        else :
            return x+1
        
fl_mdp = {}

for state in range(0, 16):

    transitions = {}

    if state in {5,7,11,12,15}:
        transitions = {action : [(1.0, state, 0, True)] for action in ["Up", "Down", "Right", "Left"]}   
        fl_mdp[state] = transitions
        continue

    for action in ["Up", "Down", "Right", "Left"]:
        todo = []
        if (action == "Up"):
            todo = ["Up", "Left", "Right"]
        elif (action == "Down"):
            todo = ["Down", "Left", "Right"]
        elif (action == "Left"):
            todo = ["Left", "Up", "Down"]
        elif (action == "Right"):
            todo = ["Right", "Up", "Down"]

        transitions[action] = []
        for task in todo:
            destiny = helper(task,state)
            transitions[action].append((1/3, destiny,1 if (destiny == 15) else 0, destiny in {5, 7, 11, 12, 15}))

    fl_mdp[state] = transitions

print("\n\nFrozen Lake\n\n")
pprint.pprint(fl_mdp)