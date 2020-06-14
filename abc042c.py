N, K = list(map(int, input().split()))
D = set(map(str, input().split()))

ans = N
while True:
  ans_set = set(str(ans))
  if ans_set & D:
    ans += 1
  else:
    break

print(ans)