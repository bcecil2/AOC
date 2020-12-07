import functools

f = open("p7.txt","r").readlines()
lines = [l.rstrip() for l in f]
e = {} 

r = ["contain",",","bags"]
count = 0

def cleanLine(l):
    r = ["contain",",","bags","bag","."]
    for x in r:
        while x in l:
            l = l.replace(x,"")
    return l
for l in lines:
    t = {}
    a = cleanLine(l).split()
    i = 2
    p = [0,""]
    c = []
    print(a)
    while i < len(a):
        if a[i] == 'no':
            break
        if a[i].isdigit() and i != 2:
            c.append((p[0],p[1]))
            p[0] = int(a[i])
            p[1] = ""
        elif i == 2:
            p[0] = int(a[i])
        else:
            p[1] += a[i]
        i += 1
    c.append((p[0],p[1]))        
    bagName = "".join([a[0],a[1]])
    e[bagName] = c

print(e)

def contains(c):
    if c == "":
        return False
    for _,c in e[c]:
        if c == "shinygold" or contains(c):
            return True
    return False

def l(v):
    t = 1
    for i,c in e[v]:
        if c == '':
            continue
        t += i*l(c)
        
    return t

print(len([color for color in e if contains(color)]))

print(l("shinygold"))

    

         



