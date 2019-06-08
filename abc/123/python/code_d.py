import itertools

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ab = [sum(e) for e in itertools.product(A, B)]
ab.sort(reverse=True)
C.sort(reverse=True)
abc = [sum(e) for e in itertools.product(ab[:K], C[:K])]
abc.sort(reverse=True)
for i in range(K):
    print(abc[i])
