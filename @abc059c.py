N = int(input())
A = list(map(int, input().split()))

ans = 0
previous_sum = A[0] # total to i - 1
for i in range(1, N):
  # if prev_sum is plus and A[i] is more minus than prev_sum, no action.
  # if prev_sum is plus and minus of A[i] is larger than or equal to prev_sum.
  if previous_sum > 0 and previous_sum + A[i] >= 0:
    # the number that need to be subtracted to meet the requirements.
    require_subtraction = previous_sum + A[i] + 1
    # correcting the current number.
    A[i] -= require_subtraction
    ans += require_subtraction
  # if prev_sum is minus and A[i] is more plus than prev_sum, no action.
  # if prev_sum is minus and minus of A[i] is more smaller than or equal to prev_sum.
  elif previous_sum < 0 and previous_sum + A[i] <= 0:
    # the number that need to be added to meet the requirements.
    require_addition = -(previous_sum + A[i] - 1)
    # correcting the current number.
    A[i] += require_addition
    ans += require_addition
  previous_sum += A[i]

print(ans)