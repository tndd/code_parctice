N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

for k in range(K):
  plus = [0 for _ in range(N)]
  for n in range(N):
    l = n - A[n]
    r = n + A[n]
    for i in range(l, r + 1):
      if 0 <= i < N:
        plus[i] += 1
  A = plus

print(' '.join(map(str, A)))
