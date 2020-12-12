from collections import defaultdict
f = open("p10.txt","r")

lines = [x.rstrip() for x in f.readlines()]

lines = [int(x)  for x in lines]
lines.append(0)
lines.append(max(lines)+3)
lines = sorted(lines)
'''
onejolt = 1 
threejolt = 1
for i in range(len(lines)-1):
    d = lines[i+1]-lines[i]
    if d == 1:
        onejolt += 1
    elif d == 3:
        threejolt += 1
print(onejolt*threejolt)
'''

DP = {}
def dp(i):
    if i == len(lines)-1:
        return 1
    #if i in DP:
    #    return DP[i]
    ans = 0
    '''
    for j in range(i+1,min(i+4,len(lines))):
        if lines[j]-lines[i] <= 3:
            ans += dp(j)
    '''
    x = lines[i]
    for j in [x+1,x+2,x+3]:
        idx = lines.index(j) if j in lines else None
        if idx != None:
            ans += dp(idx)
    #DP[i] = ans
    return ans

print(dp(0))
'''
dp = defaultdict(int)
dp[0] = 1
for x in lines:
    dp[x] += dp[x-1]+dp[x-2]+dp[x-3]
print(dp[lines[-1]])
'''
