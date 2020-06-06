N = int(input())
A = list(map(int, input().split()))

colors = [False for _ in range(8)]

# rate 3200+
allmite = 0
for i in range(N):
  if 1 <= A[i] <= 399:
    colors[0] = True
  elif 400 <= A[i] <= 799:
    colors[1] = True
  elif 800 <= A[i] <= 1199:
    colors[2] = True
  elif 1200 <= A[i] <= 1599:
    colors[3] = True
  elif 1600 <= A[i] <= 1999:
    colors[4] = True
  elif 2000 <= A[i] <= 2399:
    colors[5] = True
  elif 2400 <= A[i] <= 2799:
    colors[6] = True
  elif 2800 <= A[i] <= 3199:
    colors[7] = True  
  else:
    allmite += 1

colors_cnt = colors.count(True)
# if they are all allmite, the minimum number is 1, not 0.
ans_min = max(colors_cnt, 1)
ans_max = colors.count(True) + allmite

print(ans_min, ans_max)