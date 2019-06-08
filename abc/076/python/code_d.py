N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
v.append(0)


def get_partitioned_area(t, start, ma, end):
    raise NotImplementedError("がんばれみらいのじぶん")


ans = 0
start = 0
for i in range(N):
    area, end = get_partitioned_area(t[i], start, v[i], v[i + 1])
    ans += area

print(ans)
