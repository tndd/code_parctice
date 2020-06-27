N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

time = 0
ans = 0
while True:
  al = len(A)
  bl = len(B)
  if al > 0 and bl > 0 and (time + A[0] <= K or time + B[0] <= K):
    pass
  elif al > 0 and bl == 0 and (time + A[0] <= K):
    pass
  elif al == 0 and bl > 0 and (time + B[0] <= K):
    pass
  else:
    break
  if al > 0 and bl > 0:
    if A[0] >= B[0]:
      time += B.pop(0)
    else:
      time += A.pop(0)
  elif al > 0 and bl == 0:
    time += A.pop(0)
  elif al == 0 and bl > 0:
    time += B.pop(0)
  ans += 1

print(ans)