from math import sqrt

N = int(input())

ans = float('inf')

for a in range(1, int(sqrt(N)) + 1):
  if N % a == 0:
    A = str(a)
    B = str(N // a)
    F = max(len(A), len(B))
    ans = min(ans, F)

print(ans)