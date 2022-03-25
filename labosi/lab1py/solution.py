from algparser import parse_args, parse_ss, parse_h
from algos import bfs, ucs, astar
from heuristic import check_consistent, check_optimistic

def pretty_print_algo(algo, h, found, visited_cnt, length, cost, nodelist):
    print("# " + algo + ' ' + h)
    print("[FOUND_SOLUTION]: " + ('yes' if found else 'no'))
    if(found):
        print("[STATES_VISITED]: {}".format(visited_cnt))
        print("[PATH_LENGTH]: {}".format(length))
        print("[TOTAL_COST]: {}".format(cost))
        print("[PATH]: " + " => ".join([x.name for x in nodelist]))

def pretty_print_heuristic():
    pass

def main():
    args = parse_args()
    start, e_states, ss = parse_ss(args.ss[0])
    
    if(args.alg):
        alg = args.alg[0]
        if(alg == 'bfs'):
            solved, count, length, cost, path = bfs(start, e_states, ss)
        elif(alg == 'ucs'):
            solved, count, length, cost, path = ucs(start, e_states, ss)
        elif(alg =='astar'):
            if(not args.h):
                print("No heuristic description source specified!")
            h = parse_h(args.h[0])
            solved, count, length, cost, path = astar(start, e_states, ss, h)
        pretty_print_algo(alg.upper(), args.h[0] if args.h else "" , solved, count, length, cost, path)
    elif(args.check_optimistic or args.check_consistent):
            if(not args.h):
                print("No heuristic description source specified!")
            h = parse_h(args.h[0])
            if(args.check_optimistic):
                check_optimistic(h, ss, e_states, args.h[0])
            else:
                check_consistent(h, ss, e_states, args.h[0])
        
    

if __name__ == "__main__":
    main()