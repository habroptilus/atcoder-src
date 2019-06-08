acgt = "ACGT"
S = input()
ans = 0
s = 0
for c in S:
    if c in acgt:
        s += 1
        if c == S[-1]:
            ans = max(ans, s)
    else:
        ans = max(ans, s)
        s = 0

print(ans)
