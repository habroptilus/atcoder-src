from itertools import product
N = int(input())

for e in product(["a", "b", "c"], repeat=N):
    print("".join(e))
