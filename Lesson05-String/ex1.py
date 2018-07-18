Width = [1, 3]
Length = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(Width[0], Width[1] + 1):
    for j in range(Length[0], Length[1] + 1):
        for k in calc(i, j):
            a='{0:10}'.format(' '+str(i) + k['sign'] + str(j) + '=' + str(k['result']))
            print(a, end="|")    
    print()