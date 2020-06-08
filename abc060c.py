N, T = list(map(int, input().split()))
tl = list(map(int, input().split()))

ans = 0
prev_t = tl[0]
for t in tl[1:]:
  ans += min(t - prev_t, T)
  prev_t = t

print(ans + T)