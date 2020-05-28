class Ship:
  def __init__(self, land_from, land_to):
    self.land_from = land_from - 1
    self.land_to = land_to - 1

N, M = map(int, input().split())

ships = []
for _ in range(M):
  f, t = map(int, input().split())
  ships.append(Ship(f, t))

# 到達可能島リスト
reachable_islands = [float('inf') for _ in range(N)]
# 初期位置は到達可能なのでTrue
reachable_islands[0] = 0
# 探索予定島
search_list = [0]

# 新たな島に移動できたなら次も探索する
while len(search_list):
  now_island = search_list.pop(0)
  # 各到達可能な島ごとに移動シミュレーション
  if reachable_islands[now_island] == float('inf'):
      continue
  # 全ての船についてシミュレート
  for ship in ships:
    # 現在地の島発の船かつ目標島が到達済みでなければ移動シミュレート実行
    if now_island == ship.land_from \
       and reachable_islands[ship.land_to] > reachable_islands[ship.land_from] + 1:
      # 到達済の印をつける
      reachable_islands[ship.land_to] = reachable_islands[ship.land_from] + 1
      # 到着島を探索予定リストに追加
      search_list.append(ship.land_to)

# 最後の島が到達可能であるかを判定
if reachable_islands[N - 1] == 2:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')
