def concentration(water, suger):
  return 100 * suger / (water + suger)

WATER_A, WATER_B, SUGER_C, SUGER_D, MELT_PER_100, LIMIT = map(int, input().split())

WATER_A *= 100
WATER_B *= 100
# 砂糖の溶解率の上限
MELT_PERCENT_LIMIT = concentration(100, MELT_PER_100)

wa = wb = sc = sd = 0

water_set = set()
while wa * WATER_A <= LIMIT:
  while wb * WATER_B <= LIMIT:
    water = wa * WATER_A + wb * WATER_B
    if water <= LIMIT:
      water_set.add(water)
    wb += 1
  wb = 0
  wa += 1

suger_set = set()
while sc * SUGER_C <= LIMIT:
  while sd * SUGER_D <= LIMIT:
    suger = sc * SUGER_C + sd * SUGER_D
    if suger <= LIMIT:
      suger_set.add(suger)
    sd += 1
  sd = 0
  sc += 1

ans_suger_water = 0
ans_suger = 0
# 最大溶解率を保持するための変数
max_concentration = 0

for water in water_set:
  for suger in suger_set:
    # 砂糖水の量が0より大きく制限量以下以外の場合は次のループへ
    if not (0 < water + suger <= LIMIT):
      continue
    # 砂糖濃度計算
    suger_precent = concentration(water, suger)
    # 砂糖濃度が最高を更新かつ限界濃度を超えていなければ答えを更新
    if max_concentration <= suger_precent <= MELT_PERCENT_LIMIT:
      max_concentration = suger_precent
      ans_suger_water = water + suger
      ans_suger = suger

print(ans_suger_water, ans_suger)