l1 = []
l2 = {}

with open('day1/data.txt') as f:
    data = f.read().strip()
    for line in data.split('\n'):
        l1.append(int(line.split()[0]))
        if (int(line.split()[1]) not in l2):
            l2[int(line.split()[1])] = 1
        else:
            l2[int(line.split()[1])] += 1

res = 0

for elt in l1:
    res += elt * l2[elt] if elt in l2 else 0

print(res)
