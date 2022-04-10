
from resolution import resolution
def cooking(clauses: set, commands: set):
    for cmd in commands:
        print('\nUser\'s command:', cmd)
        clause = cmd.clause
        intent = cmd.intent
        if intent == '+':
            clauses.add(clause)
            print('Added', clause)
        elif intent == '-':
            if clause in clauses:
                clauses.remove(clause)
                print('Removed', clause)
        elif intent == '?':
            resolution(clauses.copy(), clause)
