N = int(input())
A = sorted(list(map(int, input().split())))
THE_NUM = 10**6 + 1

dp = [True] * THE_NUM

prev_num = -1
for i in A:
  # if the same number appears as before, that number cannot be counted in the answer.
  if prev_num != i:
    for j in range(i * 2, THE_NUM, i):
      dp[j] = False
  else:
    dp[i] = False
  prev_num = i

ans = 0
for i in A:
  # the same number after the second will not counted in the answer.
  if dp[i] == True:
    ans += 1

print(ans)
