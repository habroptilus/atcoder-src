class UnionFind:
    """1-index"""

    def __init__(self, n):
        self.parent = [-1] * (n + 1)  # parentは親の番号を格納。親だった時は-サイズを格納。

    # 親の番号を返す
    def root(self, A):
        if self.parent[A] < 0:
            return A
        else:
            return self.root(self.parent[A])

    # サイズを返す
    def size(self, A):
        return - self.parent[self.root(A)]

    # AとBをくっつける(直接ではなくroot(A)とroot(B)を繋げる)
    def unite(self, A, B):
        A = self.root(A)
        B = self.root(B)

        if A == B:  # 既に同じ塊内にいる
            return False

        if self.size(A) < self.size(B):
            A, B = B, A

        self.parent[A] += self.parent[B]  # サイズを更新
        self.parent[B] = A

        return True

    # AとBが同じグループに属しているかを調べる.
    def same_check(self, A, B):
        return self.root(A) == self.root(B)


N, M = map(int, input().split())

ans = N * (N - 1) // 2
result = [ans]
uf = UnionFind(N)
A = []
B = []

for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in reversed(range(1, M)):
    if not uf.same_check(A[i], B[i]):
        ans -= uf.size(A[i]) * uf.size(B[i])
        uf.unite(A[i], B[i])
    result.append(ans)


for i in reversed(result):
    print(i)
