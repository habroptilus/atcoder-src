N, Q = map(int, input().split())

S = input()
D = [0]
s = 0
for i in range(len(S) - 1):
    if S[i:i + 2] == "AC":
        s += 1
    D.append(s)

for _ in range(Q):
    l, r = map(int, input().split())
    print(D[r - 1] - D[l - 1])
