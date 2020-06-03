N, M = list(map(int, input().split()))

# execution time per one time
exe_time = 1900 * M + 100 * (N - M)
# let p be the probability of success in all case
# p = (1/2)^M

# let y be the expected value of the time taken
# y = x + (1 - p) * y
# solving the equation ...
# y = x/p
exe_time_exp = exe_time * pow(2, M)

print(exe_time_exp)