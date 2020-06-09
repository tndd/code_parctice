N = int(input())
A = list(map(int, input().split()))

ans = 0
previous_sum = A[0] # total to i - 1
now_sum = previous_sum
for i in range(1, N):
  now_sum += A[i]
  # if previous_sum is plus and now_sum is more minus than previous_sum, no action.
  # if previous_sum is plus and minus of now_sum is smaller than or equal to previous_sum.
  if previous_sum > 0 and previous_sum + now_sum >= 0:
    # the number that need to be subtracted to meet the requirements.
    require_subtraction = previous_sum - now_sum + 1
    # correcting the current number.
    A[i] -= require_subtraction
    now_sum -= require_subtraction
    ans += require_subtraction
  # if previous_sum is minus and now_sum is more plus than previous_sum, no action.
  # if previous_sum is minus and plus of now_sum is more smaller than or equal to previous_sum.
  elif previous_sum < 0 and previous_sum + now_sum <= 0:
    # the number that need to be added to meet the requirements.
    require_addition = -(previous_sum - now_sum - 1)
    # correcting the current number.
    A[i] += require_addition
    now_sum += require_addition
    ans += require_addition
  previous_sum += A[i]

print(A)
print(ans)