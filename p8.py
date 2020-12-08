import functools
import copy

f = open("p8.txt","r").readlines()
lines = [l.rstrip() for l in f]

instruct = []
acc = 0
seen = {}
for l in lines:
    x = l.split()
    if x[1][0] == '+':
        instruct.append((x[0],int(x[1][1:])))
    else:
        instruct.append((x[0],int(x[1])))

def doCmd(c,i):
    if c == "acc":
        global acc
        acc += i
        return 1
    if c == "nop":
        return 1
    if c == "jmp":
        return i


i = 0
while not seen.get((instruct[i],i),False):
    cmd = instruct[i] 
    seen[(cmd,i)] = True
    x = doCmd(cmd[0],cmd[1])
    i += x

idxs = [i for i in range(len(instruct)) if instruct[i][0] == 'nop']
idxs2 = [i for i in range(len(instruct)) if instruct[i][0] == 'jmp']


def run(ins,seen):
    i = 0
    while i < len(ins) and not seen.get((ins[i],i),False):
        cmd = ins[i] 
        seen[(cmd,i)] = True
        x = doCmd(cmd[0],cmd[1])
        i += x
    if i == len(ins):
        global acc
        print(acc)

for i in idxs:
    acc = 0
    seen = {}
    c = copy.copy(instruct)
    c[i] = ("jmp",c[i][1])
    run(c,seen)

for i in idxs2:
    acc = 0
    seen = {}
    c = copy.copy(instruct)
    c[i] = ("nop",c[i][1])
    run(c,seen)




