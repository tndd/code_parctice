N = int(input())
A = list(map(int, input().split()))

ans = 0
prev_sm = A[0] # total to i - 1
for i in range(1, N):
  # if prev_sum is plus and a is more minus than prev_sum.
  if prev_sm > 0 and prev_sm + A[i] < 0:
    pass
  # if prev_sum is plus and a is larger than or equal to prev_sum.
  elif prev_sm > 0 and prev_sm + A[i] >= 0:
    ans += prev_sm + A[i] + 1
    A[i] -= prev_sm + A[i] + 1
  # if prev_sum is minus and a is more plus than prev_sum.
  elif prev_sm < 0 and prev_sm + A[i] > 0:
    pass
  # if prev_sum is minus and a is more smaller than or equal to prev_sum.
  elif prev_sm < 0 and prev_sm + A[i] <= 0:
    ans += -(prev_sm + A[i] - 1)
    A[i] += -(prev_sm + A[i] + 1)
  prev_sm += A[i]

print(ans)