N = int(input())
a = list(map(int, input().split()))

s_a = sum(a)
if s_a % N != 0:
    ans = -1
else:
    ans = 0
    unit = s_a // N
    i = 0
    s = 0
    for e in a:
        i += 1
        s += e
        if s == i * unit:
            ans += i - 1
            i = 0
            s = 0


print(ans)
