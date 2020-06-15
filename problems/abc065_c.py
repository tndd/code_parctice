from math import factorial

N, M = list(map(int, input().split()))
THE_NUM = 10**9 + 7

combination_num = 0
# if N = M, the number of combination is 2N!M!.
if N == M:
  combination_num = 2 * factorial(N) * factorial(M)
# if |N - M| = 1, the number of combination is M!N!.
elif abs(N - M) == 1:
  combination_num = factorial(N) * factorial(M)
# if none of the above conditions,
# can't line up. so not change combination_num from 0.

print(combination_num % THE_NUM)