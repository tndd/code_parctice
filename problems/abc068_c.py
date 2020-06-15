class Ship:
  def __init__(self, land_from, land_to):
    self.land_from = land_from - 1
    self.land_to = land_to - 1

N, M = map(int, input().split())

mid_from = set()
mid_to = set()

ships = []
for _ in range(M):
  f, t = map(int, input().split())
  ship = Ship(f, t)
  if ship.land_from == 0:
    mid_from.add(ship.land_to)
  if ship.land_to == N - 1:
    mid_to.add(ship.land_from)

# 最後の島が到達可能であるかを判定
if mid_from & mid_to:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')
