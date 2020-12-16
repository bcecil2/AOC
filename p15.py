f = open("p15.txt","r")

input = [x.rstrip() for x in f.readlines()]

init = list(map(int,input[0].split(",")))


def silver(init):
    lasts = {}
    turn = 0
    last = 0
    lastd = 0
    for x in init:
        turn += 1
        lasts[x] = turn
        lastd = 0


    while turn != 2020:
        turn += 1
        last = lastd
        lastd = turn - lasts[last] if last in lasts else 0
        lasts[last] = turn

    return last 


def gold(init):
    lasts = {}
    turn = 0
    last = 0
    lastd = 0
    for x in init:
        turn += 1
        lasts[x] = turn
        lastd = 0


    while turn != 30000000:
        turn += 1
        last = lastd
        lastd = turn - lasts[last] if last in lasts else 0
        lasts[last] = turn

    return last 


print(silver(init))
print(gold(init))
