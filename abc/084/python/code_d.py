import math
N = 10**5

Q = int(input())


def eratosthenes(n):
    """n以下の素数をエラトステネスの篩によって求める."""
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


_primes = eratosthenes(N)

primes = [False] * (10**5 + 1)

for p in _primes:
    primes[p] = True

like_2017 = [False] * (10**5 + 1)

for p in _primes:
    if primes[(p + 1) // 2]:
        like_2017[p] = True


c = 0
C = [0]
for i in range(1, 10**5 + 1):
    if like_2017[i]:
        c += 1
    C.append(c)


for _ in range(Q):
    left, right = map(int, input().split())
    print(C[right] - C[left - 1])
