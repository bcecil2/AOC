inputFile = open('p3.txt', 'r')
inputLines = inputFile.readlines()
clean = []
for line in inputLines:
    clean.append(line.rstrip())
def dup(m):
    i = 0 
    new = []
    for line in m:
        new.append(line+clean[i]) 
        i += 1
    return new

curr = clean
end = len(clean)
#for i in range((end-1)//2):
#   curr = dup(curr)

x = 0
y = 0
trees = 0
while y+1 < end:
    y += 1
    x = (x + 3) % len(curr[y])
    if curr[y][x] == '#':
        trees += 1
print(trees)

def general(r,d,clean):
    end = len(clean)

    x = 0
    y = 0
    trees = 0
    while y+d < end:
        y += d
        x = (x + r) % len(clean[y]) 
        if clean[y][x] == '#':
            trees += 1
    return trees

ans = 1
test =  [(1,1),(3,1),(5,1),(7,1),(1,2)]
for r,d in test:
    ans *= general(r,d,clean) 
print(ans)
