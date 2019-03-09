N, M = map(int, input().split())
juice_list = []

for _ in range(N):
    a, b = map(int, input().split())
    juice_list.append((a, b))

juice_list.sort(key=lambda x: x[0])

juice_num = 0
money = 0
for juice in juice_list:
    if juice_num + juice[1] < M:
        money += juice[0] * juice[1]
        juice_num += juice[1]
    else:
        money += (M - juice_num) * juice[0]
        juice_num += M - juice_num
        break

print(money)
