import itertools
from collections import Counter


def get_discomfort(group_dic, color, D):
    s = 0
    for c, num in group_dic.items():
        s += D[c - 1][color - 1] * num
    return s


N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]


grids = [Counter() for _ in range(3)]

for i in range(N):
    c = list(map(int, input().split()))
    for j in range(N):
        grids[(i + j) % 3][c[j]] += 1


ans = float("inf")
for colors in itertools.permutations(list(range(C)), 3):
    colors = list(colors)
    s = 0
    for i, c in enumerate(colors):
        s += get_discomfort(grids[i], c, D)
    ans = min(ans, s)

print(ans)
