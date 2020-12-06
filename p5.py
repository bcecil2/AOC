import math
 = open("p5.txt","r")
lines = [l.rstrip() for l in f.readlines()]

def row(char,lower,upper):
    if char == 'B':
        return (math.ceil(lower + ((upper-lower)/2)),upper)
    else:
        return (lower,math.floor(lower + ((upper-lower)/2)))

def col(char,lower,upper):
   if char == 'R':
        return (math.ceil(lower + ((upper-lower)/2)),upper)
   else:
        return (lower,math.floor(lower + ((upper-lower)/2)))
list = []
maxId = 0
for line in lines:
    r = line[:7]
    cols = line[-3:]
    l = 0
    u = 127 
    for c in r:
        l,u = row(c,l,u)
    cl = 0
    cr = 7 
    for c in cols:
        cl,cr = col(c,cl,cr)
    id = l*8 + cl
    list.append(id)
    maxId = max(maxId,id)

print(maxId)
list = sorted(list)
 
for x in range(len(list)-1):
    if list[x+1] != list[x]+1:
        print(list[x])



