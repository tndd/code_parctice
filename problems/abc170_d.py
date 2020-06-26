N = int(input())
A = sorted(list(map(int, input().split())))
THE_NUM = 10**6 + 1

dp = [True] * THE_NUM

for i in A:
  for j in range(i * 2, THE_NUM, i):
    dp[j] = False

anss = [i + 1 for i, x in enumerate(A) if dp[x] == True]

print(len(anss))
