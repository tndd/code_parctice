N = int(input())
S = sorted([int(input()) for _ in range(N)])

ans = sum(S)

if ans % 10 == 0:
  # find numbers that are not multiples of 10 in order of decreasing.
  for s in S:
    if s % 10 != 0:
      ans -= s
      break
  # if all the numbers in the list are multiples of 10, the ans is 0.
  if ans == sum(S):
    ans = 0

print(ans)
