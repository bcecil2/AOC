f = open("p9.txt","r")

l = [x.rstrip() for x in f.readlines()] 

l = list(map(int,l))
pre = 25
prev = l[:pre]
i = pre 
win = 1

sub = [l[i:i+j] for i in range(len(l)) for j in range(1,len(l)-i+1)] 
 = [x for x in sub if len(x) >= 2 and sum(x) == 552655238]
ans = [30484395, 26952678, 25903382, 26433970, 27327951, 29543326, 31321247, 30139557, 31044336, 32989305, 31818413, 34730529, 35979636, 41140695, 35790623, 36286332, 44768863]

print(min(ans)+max(ans))
while i < len(l):
    cur = l[i]
    print(cur,prev)
    seen = False
    for x in prev:
        for y in prev:
            if x != y and x+y == cur:
                seen = True
    if not seen:
        print(cur)
        break
    i += 1 
    prev = l[win:win+pre]
    win += 1
