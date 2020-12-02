inputFile = open('input.txt', 'r')
inputLines = inputFile.readlines()

input = []
valid = 0
for line in inputLines:
    s = line.split()
    print(s)
    range = s[0].split('-')
    print(range)
    min = int(range[0])
    max = int(range[1])
    char = s[1][0]
    string = s[2]
    total = string.count(char)
    if (string[min-1]==char and string[max-1]!=char) or (string[min-1]!=char and string[max-1]==char):
        valid += 1

print(valid)
