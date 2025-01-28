import re

with open("day3/data.txt") as f:
    l = f.read().strip().split("\n")

t = sum([re.findall('mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', n) for n in l], [])

res = 0
flag = True
for i in t:
    if i == "do()":
        flag = True
        continue
    elif i == "don't()":
        flag = False
        continue
    if flag == False:
        continue
    n = re.search('mul\(([0-9]+),([0-9]+)\)', i)
    res += int(n.group(1).strip()) * int(n.group(2).strip())

print(res)
