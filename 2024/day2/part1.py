import re

with open("day2/data.txt") as f:
    l = f.read().strip().split("\n")

l2 = [list(map(int, re.findall("\\d+", n))) for n in l]

print(
    sum(
        all(
            1 <= abs(x - y) <= 3 for x, y in zip(n, n[1:])  # Check entre 1 et 3
        )
        and
        (
            n == sorted(n) or n == sorted(n)[::-1]   # Check croissant ou decroissant
        )
        for n in l2
    )
)
