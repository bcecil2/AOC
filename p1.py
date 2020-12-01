def ans(l):
    n = len(l)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if l[i]+l[j]+l[k] == 2020:
                    return l[i]*l[j]*l[k]

with open("p1.txt", "r") as grilled_cheese:
        lines = grilled_cheese.readlines()
        nums = []
        for l in lines:
            nums.append(int(l.rstrip()))
        print(ans(nums))
