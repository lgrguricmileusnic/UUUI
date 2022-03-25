from argparse import Namespace, ArgumentParser
import readline
from node import Node


def parse_args():
    parser = ArgumentParser()
    exclusive_group = parser.add_mutually_exclusive_group()
    parser.add_argument('--alg' ,type=str, nargs=1, action='store', choices=['bfs', 'ucs', 'astar'])
    parser.add_argument('--ss', type=str, nargs=1, action='store', metavar='ss_desc_source', required=True)
    parser.add_argument('--h', type=str, nargs=1, action='store', metavar='heuristic_desc_source')
    exclusive_group.add_argument('--check-optimistic', action='store_true')
    exclusive_group.add_argument('--check-consistent', action='store_true')

    return parser.parse_args()

def parse_ss(path):
    state_space = {}
    with open(path, 'r') as src:
        line = src.readline()
        while(line.startswith('#')): line = src.readline()
        start = line.strip()
        line = src.readline()
        while(line.startswith('#')): line = src.readline()
        end_states = line.strip('\n').split(' ')
        line = src.readline()
        while(line):
            if line.startswith('#'): 
                continue
            line = line.strip('\n')
            split = line.split(':', maxsplit=1)
            state = split[0]
            rest = ''
            if len(split) > 1:
                rest = split[1]

            if state not in state_space:
                state_space[state] = set()
            rest = rest.strip()
            if(len(rest) != 0):
                next_states = rest.split(' ')
                for next in next_states:
                    next_state = next.split(',')
                    state_space[state].add(Node(next_state[0], float(next_state[1]), None))

            line = src.readline()
    
    return Node(start, 0, None), end_states, state_space
            

def parse_h(path):
    h = {}
    with open(path, 'r', encoding='utf-8') as src:
        for line in src:
            line = line.strip('\n')
            state, value = line.split(':', maxsplit=1)
            h[state] = float(value.strip())
    
    return h