H, W = list(map(int, input().split()))
S = []
for i in range(H):
    S.append(list(input()))

def gen_dp(y, x):
    dp = [[float('inf') for _ in range(W)] for _ in range(H)]
    dp[y][x] = 0
    return dp

def dist_dp(y, x, dp):
    if (not (0 <= y < H) or not (0 <= x < W)):
        return
    if (S[y + 1][x] == '.'):
        dp[y + 1][x] = min(dp[y][x] + 1, dp[y + 1][x])
        dist_dp(y + 1, x, dp)
    if (S[y][x + 1] == '.'):
        dp[y][x + 1] = min(dp[y][x] + 1, dp[y][x + 1])
        dist_dp(y, x + 1, dp)
    if (S[y - 1][x] == '.'):
        dp[y - 1][x] = min(dp[y][x] + 1, dp[y - 1][x])
        dist_dp(y - 1, x, dp)
    if (S[y][x - 1] == '.'):
        dp[y][x - 1] = min(dp[y][x] + 1, dp[y][x - 1])
        dist_dp(y, x - 1, dp)


from pprint import pprint
for y in range(H):
    for x in range(W):
        dp = gen_dp(y, x)
        pprint(dist_dp(y, x, dp))
