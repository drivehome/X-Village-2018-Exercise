class RelationException(Exception):
    def __init__(self, err_msg):
        self.msg = err_msg
    def __str__(self):
        return ("Are you sure that {} and {} are in love with each other?".format(p1, p2))

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if (pa or pa)not in relation:
        raise Exception
    elif relation[pa] != pb:
        raise RelationException("Are you sure that {} and {} are in love with each other?".format(p1, p2))        
    
try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))
    
except RelationException as e:
    print(e)
except Exception as e:
        print(("Are you sure that {} and {} are People?".format(p1, p2)))

