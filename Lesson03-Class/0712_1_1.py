"""
#a1績效獎金
#a2加班費
#b1績效獎金
#b2加班費
#c1績效獎金
#c2加班費

if (a > 90):
    a = 9000 + 200*20
    print(a)
elif(b < 70):
    b = 6000 + 200*15
    print(b)
else:
    c = 4000 + 200*25 
    print(c)
"""
performance = 91
time = 20
bonus = 0
extra = 0

if (performance > 90):
    bonus +=8000
elif (performance < 70):
    bonus +=4000
else:
    bonus +=6000

extra = 200 * time
salary = bonus + extra

print("salary", salary)

performance = 75
time = 15
bonus = 0
extra = 0

if (performance > 90):
    bonus +=8000
elif (performance < 70):
    bonus +=4000
else:
    bonus +=6000

extra = 200 * time
salary = bonus + extra

print("salary", salary)

performance = 60
time = 25
bonus = 0
extra = 0

if (performance > 90):
    bonus +=8000
elif (performance < 70):
    bonus +=4000
else:
    bonus +=6000

extra = 200 * time
salary = bonus + extra

print("salary", salary)