import re

with open("day3/data.txt") as f:
    l = f.read().strip().split("\n")

t = sum([re.findall('mul\(.{1,3},.{1,3}\)', n) for n in l], [])

res = 0
for i in t:
    n = re.search('mul\(([0-9]+),([0-9]+)\)', i)
    res += int(n.group(1).strip()) * int(n.group(2).strip())

print(res)
