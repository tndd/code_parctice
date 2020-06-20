N, M = list(map(int, input().split()))

dp = [[0] * M for _ in range(M)]

for _ in range(M):
  a, b = list(map(int, input().split()))
  dp[a - 1][b - 1] += 1
  dp[b - 1][a - 1] += 1

print(dp)