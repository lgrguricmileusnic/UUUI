#!/usr/bin/env python3
from cProfile import label
from parsers import parse_args, parse_commands, parse_clauses
from resolution import resolution
from cooking import cooking


def main():
    args = parse_args()
    fclauses = open(args.clause_file, 'r')

    if(args.mode == 'resolution'):
        clauses, goal = parse_clauses(fclauses.readlines(), cooking_mode=False)
        fclauses.close()
        resolution(clauses, goal)
    else:
        clauses, goal = parse_clauses(fclauses.readlines(), cooking_mode=True)
        fclauses.close()
        fcmds = open(args.commands_file, 'r')
        commands = parse_commands(fcmds.readlines())
        fcmds.close()
        cooking(clauses, commands)

            
        

if __name__ == '__main__':
    main()