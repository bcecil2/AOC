f = open("p12.txt","r")

xs = [x.rstrip() for x in f.readlines()]


moves = {"N":(0,1),"S":(0,-1),
         "E":(1,0),"W":(-1,0)}


dir = "E"
cur = (0,0)
for x in xs:
    move = x[0]
    num = int(x[1:])
    x,y = cur
    if move == "F":
        dx,dy = moves[dir]
    elif move == "R":
        dirs = ["E","S","W","N"]
        i = (dirs.index(dir)+num//90)%4
        dir = dirs[i]
        continue
    elif move == "L":
        dirs = ["E","N","W","S"]
        i = (dirs.index(dir)+num//90)%4
        dir = dirs[i]
        continue
    else:
        dx,dy = moves[move]
    if not move in ["L","R"]:
        cur = (x+(dx*num),y+(num*dy))

dir = "E"
cur = (0,0)
w = (10,1)
for x in xs:
    move = x[0]
    num = int(x[1:])
    x,y = cur
    if move == "F":
        dx,dy = moves[dir]
        cur = (x+w[0]*num,y+w[1]*num)
    elif move == "L":
        wx,wy = w
        for i in range(num//90):
            wx,wy = -wy,wx
        
        w = (wx,wy)
    elif move == "R":
        wx,wy = w
        for i in range(num//90):
            wx,wy = wy,-wx
        w = (wx,wy)
    else:
        dx,dy = moves[move]
        wx,wy = w
        w = (wx+(dx*num),wy+(dy*num))
    print(cur,w)


print(abs(cur[0])+abs(cur[1]))
    

