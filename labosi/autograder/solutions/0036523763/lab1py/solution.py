from collections import deque
from algparser import parse_args, parse_ss, parse_h
from node import Node
from heapq import heappop, heappush
def pretty_print(algo, h, found, visited_cnt, length, cost, nodelist):
    print("# " + algo + ' ' + h)
    print("[FOUND_SOLUTION]: " + 'yes' if found else 'no')
    if(found):
        print("[STATES_VISITED]: {}".format(visited_cnt))
        print("[PATH_LENGTH]: {}".format(length))
        print("[TOTAL_COST]: {}".format(cost))
        print("[PATH]: " + " => ".join([x.name for x in nodelist]))

def ucs(start, e_states, ss):
    start.tcost = 0
    o = [start]
    closed = set()
    visited_cnt = -1
    while(len(o) > 0):
        current = o.pop(0)
        visited_cnt += 1
        if(current.name in e_states):
            out = current
            cost = 0
            length = 0
            path = []
            while(out):
                cost += out.cost
                length += 1
                path.append(out)
                out = out.parent
            path.reverse()
            pretty_print("UCS", "", True, visited_cnt, length, cost, path)
            return
        for tmpstate in ss[current.name]:
            state = Node(tmpstate.name, tmpstate.cost, current)
            if(state.name not in closed):
                state.tcost = current.tcost + state.cost
                o.append(state)
        o = sorted(o, key=lambda x : x.tcost)
        closed.add(current.name)
    pretty_print("UCS", "", False, 0, 0, 0, None)
    
    return
    
def bfs(start, e_states, ss):
    o = deque([start])
    closed = set()
    visited_cnt = -1
    while(len(o) > 0):
        current = o.popleft()
        visited_cnt += 1
        if(current.name in e_states):
            out = current
            cost = 0
            length = 0
            path = []
            while(out):
                cost += out.cost
                length += 1
                path.append(out)
                out = out.parent
            path.reverse()
            pretty_print("BFS", "", True, visited_cnt, length, cost, path)
            return
        for tmpstate in sorted(ss[current.name], key=lambda x: x.name):
            state = Node(tmpstate.name, tmpstate.cost, current)
            if(state.name not in closed):
                o.append(state)
        closed.add(current.name)
    pretty_print("BFS", "", False, 0, 0, 0, None)
    
    return
    
def astar(staro, e_stateo, ss, h):
    pass

def main():
    args = parse_args()
    start, e_states, ss = parse_ss(args.ss[0])

    if(args.alg):
        alg = args.alg[0]
        if(alg == 'bfs'):
            bfs(start, e_states, ss)
        elif(alg == 'ucs'):
            ucs(start, e_states, ss)
        elif(alg =='astar'):
            if(not args.h):
                print("No heuristic description source specified!")
            h = parse_h(args.h[0])
            astar(start, e_states, ss, h)
    

if __name__ == "__main__":
    main()