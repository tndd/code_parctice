N = int(input())
A = sorted(list(map(int, input().split())))
THE_NUM = 10**6 + 1

dp = [True] * (THE_NUM)

for i in range(2, THE_NUM):
  for j in range(i * 2, THE_NUM, i):
    dp[j] = False

print(dp)

# anss = [i + 1 for i, x in enumerate(A[2:]) if dp[x] == False]

# print(anss)

# ans = 0
# for i in range(N):
#   is_divide = False
#   for j in range(i):
#     if A[i] % A[j] == 0:
#       is_divide = True
#       break
#   if is_divide == False:
#     ans += 1

# # same number pattern.
# if A[0] in A[1:]:
#   ans -= 1

# # single number pattern.
# if N == 1:
#   ans -= 1

# print(ans)