N = int(input())
a = list(map(int, input().split()))

min_diff = float('inf')
a_sum = sum(a)
l_sum = 0

for i in range(N - 1):
  l_sum += a[i]
  min_diff = min(min_diff, abs(l_sum * 2 - a_sum))

print(min_diff)
