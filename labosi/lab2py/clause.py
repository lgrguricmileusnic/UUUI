
class Clause():
    def __init__(self) -> None:
        self.literals = set()
        #self.id = -1;
        self.parents = set()
        self.nil = False
    def __repr__(self) -> str:
        return 'NIL' if self.nil else ' v '.join(map(str, self.literals))

    def __str__(self) -> str:
        return 'NIL' if self.nil else ' v '.join(map(str, self.literals))
    
    def __eq__(self, object) -> bool:
        return self.literals == object.literals
    
    def __hash__(self) -> int:
        hsh = 0
        for lt in self.literals:
            hsh += hash(lt)
        
        return hash((hsh, self.nil))
    
    def is_subsumed_by(self, other) -> bool:
        return other.literals.issubset(self.literals)
    
    def is_tautology(self):
        for lt1 in self.literals:
            tmp = Literal()
            tmp.name = lt1.name
            tmp.negated = not lt1.negated
            if tmp in self.literals:
                return True
        return False
        

class Literal():
    def __init__(self) -> None:
        self.name = "";
        self.negated = False

    def __repr__(self) -> str:
        return ('~' if self.negated else '' ) + self.name

    def __str__(self) -> str:
        return ('~' if self.negated else '' ) + self.name

    def __hash__(self) -> int:
        return (self.name, self.negated).__hash__()
    
    def __eq__(self, object) -> bool:
        return self.name == object.name and self.negated == object.negated
            