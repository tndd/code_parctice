oni, oni_spd = list(map(int, input().split()))
child, child_spd = list(map(int, input().split()))
T = int(input())

# 4 dist_from_oni(+)
# -1 ofs_spd(-)
# T = 5
# expect false
# -5 >= 4

# -4
# 1
# T = 5
# expect false
# 5 <= -4

dist_from_oni = child - oni     # -4
ofs_spd = oni_spd - child_spd   # -1
# T = 5
# -5 >= -4
if dist_from_oni >= 0 and ofs_spd >= 0 or dist_from_oni >= 0 and ofs_spd <= 0:
  if ofs_spd * T >= dist_from_oni:
    print('YES')
  else:
    print('NO')
elif dist_from_oni <= 0 and ofs_spd <= 0 or dist_from_oni <= 0 and ofs_spd >= 0:
  if ofs_spd * T <= dist_from_oni:
    print('YES')
  else:
    print('NO')
