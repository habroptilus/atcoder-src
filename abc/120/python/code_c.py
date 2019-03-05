S = input()

d = [0, 0]
for c in S:
    d[int(c)] += 1

print(2 * min(d))
