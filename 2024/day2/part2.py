import re

with open("day2/data.txt") as f:
    l = f.read().strip().split("\n")

l2 = [list(map(int, re.findall("\\d+", n))) for n in l]

print(
    sum(
        any(
            all(
                1 <= abs(x - y) <= 3 for x, y in zip((n[:i] + n[i + 1:]), (n[:i] + n[i + 1:])[1:])
            )
            and
            (
                (n[:i] + n[i + 1:]) == sorted((n[:i] + n[i + 1:])) or
                (n[:i] + n[i + 1:]) == sorted((n[:i] + n[i + 1:]))[::-1]
            )
            for i in range(len(n))
        )
        for n in l2
    )
)
