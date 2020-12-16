from collections import defaultdict
from functools import reduce

f = open("p14.txt","r")

l = [x.rstrip() for x in f.readlines()]

addrs = defaultdict(int) 

def getIdx(s):
    idxs = []
    for i,c in enumerate(s):
        if c == "X":
            idxs.append(i)
    return idxs
def change(x,y):
    if x == "0":
        return y
    if x == "1":
        return x
    if x == "X":
        return x

b = [2**i for i in range(36)]

def gen(L):
    bs = []
    for i in range(L):
        b = bin(i)[2:]
        bs.append("0"*(len(bin(L-1)[2:])-len(b))+b)
    return bs


def toDec(num):
    return sum([x for x,y in zip(b,num[::-1]) if y == "1"])    

#print(gen(2**4))
def genAddrs(num,val):
    idxs = getIdx(num)
    bs = gen(2**len(idxs))
    l = list(num)
    for b in bs:
        j = 0
        for i in idxs:
            l[i] = b[j]
            j+=1
        #print(l)
        addrs[toDec("".join(l))] = toDec(val)

     
    
addr = None
val = None
for x in l:
    t = x.split("=")
    if '[' in t[0]:
        addr = bin(int(t[0][4:-2]))[2:]
        addr = "0"*(36-len(addr))+addr
        val = t[1].strip()
        val = bin(int(val))[2:]
        val = "0"*(36-len(val))+val
        #print(val)
    else:
        mask = t[1].strip()    
        continue
        #print(mask)
    if addr and val:
        masked = list(map(lambda x: change(*x),zip(mask,addr)))
        #print("".join(masked))
        genAddrs("".join(masked),val)

#print(addrs)
print(sum(addrs.values()))

