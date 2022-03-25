from algos import ucs
from node import Node
def check_optimistic(h, ss, e_states, name):
    print("# HEURISTIC-OPTIMISTIC " + name)
    z = True
    for k in h:
        solved, count, length, cost, path = ucs(Node(k, 0, None), e_states, ss)
        if h[k] <= cost:
            print('[CONDITION]: [OK] h({}) <= h*: {} <= {}'.format(k, h[k], cost))
        else:
            z = False
            print('[CONDITION]: [ERR] h({}) <= h*: {} <= {}'.format(k, h[k], cost))
    print("[CONCLUSION]: Heuristic is " + ("not" if not z else "") + " optimistic.")

def check_consistent(h, ss, e_states, name):
    print("# HEURISTIC-CONSISTENT " + name)
    z = True
    for s1 in ss:
        for s2 in ss[s1]:
            if h[s1] <= h[s2.name] + s2.cost:
                print('[CONDITION]: [OK] h({}) <= h({}) + c: {} <= {} + {}'.format(s1, s2.name, h[s1], h[s2.name], s2.cost))
            else:
                z = False
                print('[CONDITION]: [ERR] h({}) <= h({}) + c: {} <= {} + {}'.format(s1, s2.name, h[s1], h[s2.name], s2.cost))
    print("[CONCLUSION]: Heuristic is " + ("not" if not z else "") + " consistent.")
    