N = int(input())
A = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
  is_divide = False
  for j in range(i):
    if A[i] % A[j] == 0:
      is_divide = True
      break
  if is_divide == False:
    ans += 1

if A[0] in A[1:]:
  ans -= 1

print(ans)