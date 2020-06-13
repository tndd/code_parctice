oni, oni_spd = list(map(int, input().split()))
child, child_spd = list(map(int, input().split()))
T = int(input())

dist = abs(child - oni)
ofs_spd = oni_spd - child_spd

if ofs_spd * T >= dist and dist / ofs_spd % 2 == 0 and 0 <= dist / ofs_spd <= T:
    print('YES')
else:
  print('NO')