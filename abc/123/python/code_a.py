A = []
for i in range(5):
    A.append(int(input()))

k = int(input())

print("Yay!" if A[-1] - A[0] <= k else ":(")
