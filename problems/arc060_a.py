card_num, target_average = list(map(int, input().split()))
x = list(map(int, input().split()))

dp = [[[0]*(card_num * target_average + 1) for _ in range(card_num + 1)] for _ in range(card_num + 1)]
dp[0][0][0] = 1

# number of cards to be ranged.
for i in range(card_num):
  # number of cards to be selected.
  for n in range(card_num):
    # total sum.
    for sm in range(card_num * target_average):
      if dp[i][n][sm] == 0:
        continue
      # pattern use xi
      dp[i + 1][n][sm] += dp[i][n][sm]
      # pattern not use xi
      if sm + x[i] <= card_num * target_average:
        dp[i + 1][n + 1][sm + x[i]] += dp[i][n][sm]

ans = 0
for n in range(1, card_num + 1):
  ans += dp[card_num][n][n * target_average]

print(ans)
