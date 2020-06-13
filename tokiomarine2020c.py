N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
empty = [0 for _ in range(N)]

for k in range(min(K, 1000)):
  plus = empty[:]
  for n in range(N):
    l = n - A[n]
    r = n + A[n]
    for i in range(l, r + 1): 
      if 0 <= i < N:
        plus[i] += 1
  A = plus

print(' '.join(map(str, A)))
