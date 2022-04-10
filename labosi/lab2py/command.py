from clause import Clause


class Command():
    def __init__(self) -> None:
        self.clause = Clause()
        self.intent = ''

    def __repr__(self) -> str:
        return ' '.join([str(self.clause), self.intent])
    
    def __str__(self) -> str:
        return ' '.join([str(self.clause), self.intent])