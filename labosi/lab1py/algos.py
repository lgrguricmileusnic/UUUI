from heapq import heappop, heappush
from node import Node, FCostNode
from collections import deque



def climb_path(current):
    out = current
    cost = 0.0
    length = 0
    path = []
    while(out):
        cost += out.cost
        length += 1
        path.append(out)
        out = out.parent
    path.reverse()
    return length, cost, path


def ucs(start, e_states, ss):
    start.gcost = 0
    o = [] 
    id = 0
    heappush(o, (0, id, start))
    closed = set()
    visited_cnt = -1
    while(len(o) > 0):
        current = heappop(o)[2]
        visited_cnt += 1
        if(current.name in e_states):
            length, cost, path = climb_path(current=current)
            return True, visited_cnt, length, cost, path
            
            
        for tmpstate in ss[current.name]:
            state = Node(tmpstate.name, tmpstate.cost, current)
            if(state.name not in closed):
                id += 1
                state.gcost = current.gcost + state.cost
                heappush(o, (state.gcost, id, state))
        closed.add(current.name)
    return False, 0, 0, 0, None
    
def bfs(start, e_states, ss):
    o = deque([start])
    closed = set()
    visited_cnt = -1
    while(len(o) > 0):
        current = o.popleft()
        visited_cnt += 1
        if(current.name in e_states):
            length, cost, path = climb_path(current=current)
            return True, visited_cnt, length, cost, path

        for tmpstate in sorted(ss[current.name], key=lambda x: x.name):
            state = Node(tmpstate.name, tmpstate.cost, current)
            if(state.name not in closed):
                o.append(state)
        closed.add(current.name)
    return False, 0, 0, 0, None


def astar(start, e_states, ss, h):
    start = FCostNode(start.name, start.cost, start.parent)
    start.gcost = 0
    start.fcost = h[start.name] 
    open = [] 
    gdict = {}
    gdict[start] = start.gcost
    
    heappush(open, start)
    closed = set()
    clsopn = set([start])
    visited_cnt = 0
    while(open):
        current = heappop(open)
        clsopn.remove(current)
        visited_cnt += 1
        if(current.name in e_states):
            length, cost, path = climb_path(current=current)
            return True, visited_cnt, length, cost, path

        closed.add(current)
        clsopn.add(current)
        for tmpstate in ss[current.name]:
            state = FCostNode(tmpstate.name, tmpstate.cost, current)
            state.gcost = current.gcost + state.cost
            if state in clsopn:
                if state in closed:
                    if  gdict[state] < state.gcost:
                        continue
                    else:
                        clsopn.remove(state)
                        closed.remove(state)
                else:
                    if gdict[state] < state.gcost:
                        continue
                    else:
                        clsopn.remove(state)
                        open.remove(state)
                         
            state.fcost = state.gcost + h[state.name]
            gdict[state] = state.gcost
            heappush(open, state)
            clsopn.add(state)
    return False, 0, 0, 0, None