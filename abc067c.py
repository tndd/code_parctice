N = int(input())
a = list(map(int, input().split()))

min_diff = float('inf')

for i in range(1, N):
  l_sum = sum(a[:i])
  r_sum = sum(a[i:])
  min_diff = min(min_diff, abs(l_sum - r_sum))

print(min_diff)
