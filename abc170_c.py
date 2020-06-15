X, N = list(map(int, input().split()))
P = list(map(int, input().split()))

ans = float('inf')
cnt = 0
while ans == float('inf'):
  ans_plus = X + cnt
  ans_minus = X - cnt
  if not ans_plus in P:
    ans = ans_plus
  if not ans_minus in P:
    ans = min(ans, ans_minus)
  cnt += 1

print(ans)