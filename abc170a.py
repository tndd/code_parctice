X = list(map(int, input().split()))

for i in range(len(X)):
  if X[i] == 0:
    print(i + 1)
    break