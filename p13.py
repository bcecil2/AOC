f = open("p13.txt","r")
l =  [x.rstrip() for x in f.readlines()]
time = int(l[0])
ids = []
for i,x in enumerate(l[1].split(",")):
    if x!="x":
        ids.append((i,int(x)))

N = 1
for _,n in ids:
    N *= n

nis = list(map(lambda x: x[1],ids))
ais = list(map(lambda x: -x[0],ids))

def gcdExtended(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

yis = [N//ni for ni in nis]

def invert(y,n):
    g,x,y = gcdExtended(y,n)
    if x < 0:
        return n - abs(x)
    else:
        return x
zis = list(map(lambda x: invert(x[0],x[1]), zip(yis,nis)))

print(nis)
print(N)
print(ais)
print(yis)
#print(gcdExtended(11,26))
print(sum([ais[i]*yis[i]*zis[i] for i in range(len(ais))])%N)
'''
def getTime(x):
    i = 0
    while i <= time:
        i += x
    return (i,x)


t,id = min(list(map(getTime,ids)))
print((t-time)*id)
'''
