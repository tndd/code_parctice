from collections import Counter

n = int(input())
A = list(map(int, input().split()))

# 長さと個数の辞書
length_num = Counter(A)
# 長い順からの長さのリスト
lengths = sorted(list(length_num.keys()), reverse=True)

ans = 0
sides = []

# 長い辺の順にループ
for l in lengths:
  if len(sides) == 2:
    break
  if length_num[l] >= 4:
    ans = l * l
    break
  if length_num[l] >= 2:
    sides.append(l)

if len(sides) == 2:
  ans = sides[0] * sides[1]

print(ans)
