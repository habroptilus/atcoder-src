S = input()
c = {e: 0 for e in list("ABCDEF")}
for e in S:
    c[e] += 1
print(" ".join([str(c[e]) for e in list("ABCDEF")]))
