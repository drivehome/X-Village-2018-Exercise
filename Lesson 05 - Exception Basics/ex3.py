#test3
class RelationException(Exception):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return self.p1.p2
        
a = RelationException("Mommy", "Daddy")
try:
    raise a
except RelationException as e:
    print("RelationException", "Are you sure that" + a.p1 + "and" + a.p2 + "are in love with each other?")
