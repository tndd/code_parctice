N = int(input())
A = sorted(list(map(int, input().split())))

dp = [False] * (10**6 + 1)

for i in range(2, 10**6 + 1):
  for j in range(i + 1, 10**6 + 1):
    if dp[j] == False and j % i == 0:
      dp[j] = True

anss = [i + 1 for i, x in enumerate(A[2:]) if dp[x] == False]

print(anss)

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