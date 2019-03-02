from itertools import combinations
c = combinations(list(map(int, input().split())), 3)

hoge = sorted([sum(e) for e in c], reverse=True)
print(hoge[2])
