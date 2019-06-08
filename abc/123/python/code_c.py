N = int(input())
lowest = float("inf")
for i in range(5):
    lowest = min(lowest, int(input()))


print(-(-N // lowest) + 4)
