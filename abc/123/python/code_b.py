import itertools
C = []
for i in range(5):
    C.append(int(input()))

ans = float("inf")
for order in itertools.permutations(C, 5):
    total = 0
    for c in order:
        if total % 10 != 0:
            total = (total // 10 + 1) * 10
        total += c

    ans = min(total, ans)

print(ans)
