S = input()
dp = [[None] * 4 for _ in range(len(S) + 1)]
next_str = ["A", "B", "C"]
for i, s in enumerate(reversed(S)):
    for j in range(4):
        if j == 3 and i == len(S):
            dp[i][j] = 1
        elif i == len(S):
            dp[i][j] = 0
        elif j == 3:
            if s == "?":
                dp[i][j] = 3 * dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]
        else:
            if s == "?":
                m_1 = 3
                m_2 = 1
            else:
                m_1 = 1
                if s == next_str[j]:
                    m_2 = 1
                else:
                    m_2 = 0
            dp[i][j] = m_1 * dp[i + 1][j] + m_2 * dp[i + 1][j + 1]


print(dp)
print(dp[0][0])
