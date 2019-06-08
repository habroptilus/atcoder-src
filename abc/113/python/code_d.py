import itertools
H, W, K = map(int, input().split())

dp = [[0] * W for _ in range(H + 1)]
dp[0][0] = 1
