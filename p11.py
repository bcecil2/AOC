import copy
f = open("p11.txt","r")

xs = [x.rstrip() for x in f.readlines()]


moves ={}


def findAdj(row,col):
    total = []
    #L
    left = col-1
    while left >= 0:
        s = xs[row][left]
        if s != ".":
            total.append((row,left))
            break
        left -= 1

    #R
    right = col+1
    while right < len(xs[row]):
        s = xs[row][right]
        if s != ".":
            total.append((row,right))
            break
        right += 1
    #U

    up = row-1 
    while up >= 0:
        s = xs[up][col]
        if s != ".":
            total.append((up,col))
            break
        up -= 1

    #D

    down = row+1
    while down < len(xs):
        s = xs[down][col]
        if s != ".":
            total.append((down,col))
            break
        down += 1


    #LUD
    ludx = row-1
    ludy = col-1
    while ludx >= 0 and ludy >= 0:
        s = xs[ludx][ludy]
        if s != ".":
            total.append((ludx,ludy))
            break
        ludx -= 1
        ludy -= 1


    #LLD
    lldx = row+1
    lldy = col-1
    while lldx < len(xs) and lldy >= 0:
        s = xs[lldx][lldy]
        if s != ".":
            total.append((lldx,lldy))
            break
        lldx += 1
        lldy -= 1


    #RUP
    rudx = row-1
    rudy = col+1
    while rudx >= 0 and rudy < len(xs[row]):
        s = xs[rudx][rudy]
        if s != ".":
            total.append((rudx,rudy))
            break
        rudx -= 1
        rudy += 1


    #RLD
    rldx = row+1
    rldy = col+1
    while rldx < len(xs) and rldy < len(xs[row]):
        s = xs[rldx][rldy]
        if s != ".":
            total.append((rldx,rldy))
            break
        rldx += 1
        rldy += 1


    return total

#print(findAdj(4,3))

def move(row,col,moves):
    val = []
    x = row
    y = col
    cords = findAdj(row,col) 
    for p in cords:#[(x+1,y),(x-1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y-1),(x-1,y+1)]:
        x,y = p
        if 0 <= x < len(xs) and  0 <= y < len(xs[x]):
            val.append(p)
    if xs[row][col] == "L" and all([xs[p[0]][p[1]] == "L" or xs[p[0]][p[1]] == "." for p in val]):
        moves[(row,col)] = "#"
    elif xs[row][col] == "#" and len([1 for p in val if xs[p[0]][p[1]] == "#"])>=5:
        moves[(row,col)] = "L"
    else:
        moves[(row,col)] = xs[row][col]

prev = None
cur = xs
count = 0
while prev != cur: 
    print(1)
    for x in range(len(cur)):
        for y in range(len(cur[x])):
            move(x,y,moves)
   
    prev = copy.deepcopy(cur)
    for x in range(len(cur)):
        row = ""
        for y in range(len(cur[x])):
            row += moves[(x,y)]
        cur[x] = row

    
seats = 0
for x in range(len(cur)):
    for y in range(len(cur[x])):
        if cur[x][y] == "#":
            seats += 1
print(seats)



