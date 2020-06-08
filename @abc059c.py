N = int(input())
A = list(map(int, input().split()))

ans = 0
prev_sm = A[0] # total to i - 1
for i in range(1, N):
  # if prev_sum is plus and A[i] is more minus than prev_sum.
  if prev_sm > 0 and prev_sm + A[i] < 0:
    prev_sm += A[i]
  # if prev_sum is plus and A[i] is larger than or equal to prev_sum.
  elif prev_sm > 0 and prev_sm + A[i] >= 0:
    diff = abs(prev_sm + A[i] + 1)
    prev_sm += A[i]
    ans += diff
    A[i] -= diff
  # if prev_sum is minus and A[i] is more plus than prev_sum.
  elif prev_sm < 0 and prev_sm + A[i] > 0:
    prev_sm += A[i]
  # if prev_sum is minus and A[i] is more smaller than or equal to prev_sum.
  elif prev_sm < 0 and prev_sm + A[i] <= 0:
    diff = abs(prev_sm + A[i] - 1)
    prev_sm += A[i]
    ans += diff
    A[i] += diff

print(ans)