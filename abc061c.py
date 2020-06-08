N, K = list(map(int, input().split()))

# a number counter that can appear on a number line.
n_counter = [0 for _ in range(10**5 + 1)]
for i in range(N):
  a, b = map(int, input().split())
  n_counter[a] += b

# ask for K.
n_sum = 0
for i, n in enumerate(n_counter):
  n_sum += n
  if n_sum >= K:
    print(i)
    break
