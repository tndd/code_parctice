oni, oni_spd = list(map(int, input().split()))
child, child_spd = list(map(int, input().split()))
T = int(input())

dist = child - oni
ofs_spd = oni_spd - child_spd

if ofs_spd * T >= dist:
  print('YES')
else:
  print('NO')