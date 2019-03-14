N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append({"w": w, "v": v})

dp = [[0] * (W + 1) for _ in range(N + 1)]


for i in range(N):
    item_w = items[i]["w"]
    item_v = items[i]["v"]
    for w in range(W + 1):
        if w >= item_w:
            dp[i + 1][w] = max(dp[i][w - item_w] + item_v, dp[i][w])
        else:
            dp[i + 1][w] = dp[i][w]


print(dp[N][W])
