N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

L = sorted(A + B)

time = 0
ans = 0
for x in L:
  if time + x <= K:
    ans += 1
    time += x
  else:
    break
print(ans)