N = int(input())


def is_valid(last_4):
    cand = [last_4]
    for i in range(3):
        cand.append(last_4[:i] + last_4[i + 1] + last_4[i] + last_4[i + 2:])

    for m in cand:
        if "AGC" in m:
            return False
    return True


memo = [{} for i in range(N + 1)]
mod = 10**9 + 7


def dfs(index, last_3):
    if last_3 in memo[index].keys():
        return memo[index][last_3]
    elif index == N:
        return 1
    else:
        s = 0
        for c in "AGCT":
            if is_valid(last_3 + c):
                s = (s + dfs(index + 1, last_3[1:] + c)) % mod
        memo[index][last_3] = s
        return s


print(dfs(0, "HHH"))
