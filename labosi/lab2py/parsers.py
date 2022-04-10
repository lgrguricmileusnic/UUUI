import argparse

from clause import Clause, Literal
from command import Command

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['resolution', 'cooking'])
    parser.add_argument('clause_file')
    parser.add_argument('commands_file', nargs='?', default="", help="argument required in cooking mode")
    args = parser.parse_args()
    if args.mode == 'cooking':
        if (args.commands_file == ""):
            parser.print_help()
            exit(1)
    else:
        if(args.commands_file != ""):
            parser.print_help()
            exit(1)

    
    return args

def parse_clauses(lines, cooking_mode):
    clauses = set()
    goal = None
    for id, l in enumerate(lines):
        if '#' in l:
            continue
        l = l.lower()
        clause = Clause()
        literals = l.split(' v ')
        for lt in literals:
            literal = Literal()
            lt.strip()
            lt = lt.removesuffix('\n')
            if lt.startswith('~'):
                literal.name = lt[1:]
                literal.negated = True
            else:
                literal.name = lt
                literal.negated = False
            clause.literals.add(literal)
            
        if id == len(lines) - 1 and not cooking_mode:
            goal = clause
        else:
            clauses.add(clause)
    return clauses, goal;
        
        


def parse_commands(lines):
    commands = []
    for id, l in enumerate(lines):
        if '#' in l:
            continue
        command = Command()
        command.clause = Clause()
        l = l.removesuffix('\n').lower()
        command.intent = l[-1:]
        l = l[:-2]
        literals = l.split(' v ')
        for lt in literals:
            literal = Literal()
            lt.strip()
            lt = lt.removesuffix('\n')
            lt = lt.lower()
            if lt.startswith('~'):
                literal.name = lt[1:]
                literal.negated = True
            else:
                literal.name = lt
                literal.negated = False
            command.clause.literals.add(literal)
        commands.append(command)
    return commands;
    
