
from clause import Clause, Literal

NIL = Clause()
NIL.nil = True

def create_starting_set(clauses: set, goal: Clause) -> set:
    #goal = sorted(clauses, key=lambda c : c.id)[-1:][0]
    #clauses.remove(goal)
    negated_goal = set()
    for lt in goal.literals:
        newclause = Clause()
        newliteral = Literal()
        newliteral.name = lt.name
        newliteral.negated = not lt.negated
        newclause.literals.add(newliteral)
        clauses.add(newclause)
        negated_goal.add(newclause)
    return negated_goal

def factorisation(clauses: set):
    tautologies = set()
    for c in clauses:
        if c.is_tautology():
            tautologies.add(c)
    clauses.difference_update(tautologies)


def apply_deletion_strategy(clauses: set):
    subsumed_clauses = set()
    for c1 in clauses:
        for c2 in clauses:
            if c1 != c2:
                if c1.is_subsumed_by(c2):
                    subsumed_clauses.add(c1)

    clauses.difference_update(subsumed_clauses)

    factorisation(clauses)
    
def sos_based_selection(clauses, sos):
    all_clauses = sos.union(clauses)
    result = set()

    for c1 in sos:
        for c2 in all_clauses:
            if c1 != c2:
                result.add((c1,c2))

    return result
    

def select_clauses(clauses, sos):
    apply_deletion_strategy(clauses)
    return sos_based_selection(clauses, sos)

def pl_resolve(c1: Clause, c2: Clause):
    resolvents = set()
    all_literals = c1.literals.union(c2.literals)
    nil = False
    for lt1 in c1.literals:
        for lt2 in c2.literals:
            if lt1.name == lt2.name and lt1.negated != lt2.negated:
                clause = Clause()
                clause.literals = all_literals.difference([lt1,lt2])
                clause.parents.update(set([c1,c2]))
                if len(clause.literals) == 0:
                    clause.nil = True
                    nil = True
                resolvents.add(clause)
    return resolvents, nil

def pretty_print(conclusion: bool, nil_clause: Clause, goal):
    starting_clauses = []
    derived_clauses = []
    derived_clauses.append(nil_clause)
    left = [nil_clause]
    if not conclusion:
        print('[CONCLUSION]: {} is unknown'.format(goal))
        return
    while(True):
        if len(left) == 0:
            break
        current = left.pop(0)
        for p in current.parents:
            if len(p.parents) == 0:
                if p not in starting_clauses:
                    starting_clauses.append(p)
            else:
                if p not in derived_clauses:
                    derived_clauses.append(p)
            if p in left:
                left.remove(p)
            left.append(p)
    derived_clauses.reverse()

    for i in range(len(starting_clauses)):
        print('{}. {}'.format(i + 1, starting_clauses[i]))
    print('===============')
    for i in range(len(derived_clauses)):
        clause = derived_clauses[i]
        parent_indexes = []
        for j, parent in enumerate(clause.parents):
            if parent in starting_clauses:
                parent_indexes.append(starting_clauses.index(parent) + 1)
            elif parent in derived_clauses:
                parent_indexes.append(derived_clauses.index(parent) + 1 + len(starting_clauses))
        parent_indexes.sort()
        print('{}. {} ({}, {})'.format(i + 1 + len(starting_clauses), derived_clauses[i], parent_indexes[0], parent_indexes[1]))
    print('===============')
    print('[CONCLUSION]: {} is true'.format(goal))

def resolution(clauses: set, goal: Clause):
    negated_goal = create_starting_set(clauses, goal)
    new_clauses = set()
    while(1):
        for c1, c2 in select_clauses(clauses, new_clauses.union(negated_goal)):
            resolvents, contains_nil = pl_resolve(c1, c2)
            if contains_nil > 0:
                nils = [x for x in resolvents if x.nil]
                pretty_print(True, nils[0], goal)
                return True
            new_clauses.update(resolvents)
        apply_deletion_strategy(new_clauses)
        if new_clauses.issubset(clauses):
            pretty_print(False, None, goal)
            return False
        clauses.update(new_clauses)



