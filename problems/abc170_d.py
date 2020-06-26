N = int(input())
A = sorted(list(map(int, input().split())))
THE_NUM = 10**6 + 1

dp = [True] * THE_NUM

for i in A:
  for j in range(i * 2, THE_NUM, i):
    dp[j] = False

ans = 0
prev_num = -1
for i, x in enumerate(A):
  # the same number after the second will not counted in the answer.
  if dp[x] == True and prev_num != i:
    ans += 1

# if they are all the same number, the answer is 0.
if A[0] == A[-1]:
  ans = 0

print(ans)
