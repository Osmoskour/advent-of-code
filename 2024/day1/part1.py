l1 = []
l2 = []

with open('day1/distance_data.txt') as f:
    data = f.read().strip()
    for line in data.split('\n'):
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))

l1.sort()
l2.sort()

res = 0

for i in range(len(l1)):
    res += abs(l1[i] - l2[i])

print(res)
