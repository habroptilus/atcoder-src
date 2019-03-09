A, B = map(int, input().split())


def judge(x, phase):
    if x < phase // 2 or (x - phase // 2) % 2 == 1:
        return 0
    else:
        return 1


result = []

if (B // 2 + B % 2 - ((A - 1) // 2 + (A - 1) % 2)) % 2 == 0:
    result.append("0")
else:
    result.append("1")

for i in range(2, len(bin(B)[2:]) + 1):
    phase = 2**i
    b = B % phase
    a = (A - 1) % phase
    if judge(a, phase) == judge(b, phase):
        result.append("0")
    else:
        result.append("1")

result.reverse()
print(int("".join(result), 2))
