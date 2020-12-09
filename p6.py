
f = open("p6.txt","r").read().split("\n\n")

z = [[{*x} for x in line.split()] for line in f]
x = list(map(lambda x: functools.reduce(lambda a,b: a.union(b),x),z))
y = list(map(lambda x: functools.reduce(lambda a,b: a.intersection(b),x),z))

print(sum(map(lambda x: len(x),x)))
print(sum(map(lambda x: len(x),y)))
