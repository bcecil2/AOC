f = open("p4.txt","r")
lines = [l.rstrip() for l in f.readlines()]

keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

def isValid(key,val):
    if key == "byr":
        val = int(val)
        if val >=1920 and val <= 2002:
            return 1
        else:
            return 0
    if key == "iyr":
        val = int(val)
        if val >= 2010 and val <= 2020:
            return 1
        else:
            return 0
    if key == "eyr":
        val = int(val)
        if val >= 2020 and val <= 2030:
            return 1
        else:
            return 0
    if key == "hgt":
        if val[-2:] != "cm" and val[-2:] != "in":
            return 0
        size = int(val[:-2])
        unit = val[-2:]
        if unit == "":
            return 0
        if unit == "cm":
            if size >= 150 and size <= 193:
                return 1
            else:
                return 0
        else:
            if size >= 59 and size <= 76:
                return 1
            else:
                return 0
    if key == "hcl":
        if val[0] != '#':
            return 0
        nums = [0,1,2,3,4,5,6,7,8,9]
        chars = ['a','b','c','d','e','f']
        count = 0
        for c in val[1:]:
            if c in chars: 
                count += 1
            elif int(c) in nums:
                count += 1
            else:
                return 0
        if count == 6:
            print(val)
            return 1
        else:
            return 0
    if key == "ecl":
        if val in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return 1
        else:
            return 0
    if key == "pid":
        if len(val) == 9 and val.isdigit():
            return 1
        else:
            return 0
    if key == "cid":
        return 1
    return 0


def getFields(line):
    fields = []
    l = line.split()
    for x in l:
        fields.append(x.split(':')[0])

    return fields

def getBoth(line):
    fields = []
    l = line.split()
    for x in l:
        t = x.split(':')
        fields.append((t[0],t[1]))
    return fields

total = 0
count = 0
seenCid = False
i = 0
keys = []
while i < len(lines):
    while i < len(lines) and lines[i] != "":
        keys += getFields(lines[i])
        i += 1
    #print(keys)
    for x in keys:
        count += 1
        if x == "cid":
            seenCid = True
    if (count == 8) or (count == 7 and (seenCid == False)):
        total += 1
    i += 1
    keys = []
    count = 0
    seenCid = False


total = 0
count = 0
seenCid = False
i = 0
keys = []
while i < len(lines):
    while i < len(lines) and lines[i] != "":
        keys += getBoth(lines[i])
        i += 1
    print(keys)
    for (k,v) in keys:
        count += isValid(k,v)
        if k == "cid":
            seenCid = True
    if (count == 8) or (count == 7 and (seenCid == False)):
        total += 1
    i += 1
    keys = []
    count = 0
    seenCid = False

print(total)
