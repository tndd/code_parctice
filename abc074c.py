def concentration(water, suger):
  return 100 * suger / (water + suger)

WATER_A, WATER_B, SUGER_C, SUGER_D, MELT_PER_100, LIMIT = map(int, input().split())

WATER_A *= 100
WATER_B *= 100
MELT_PERCENT = concentration(100, MELT_PER_100)

max_concentration = 0
ans_suger_water = 0
ans_suger = 0

wa = wb = sc = sd = 0

water_list = []
while wa * WATER_A <= LIMIT:
  while wb * WATER_B <= LIMIT:
    water = wa * WATER_A + wb * WATER_B
    if water <= LIMIT:
      water_list.append(water)
    wb += 1
  wb = 0
  wa += 1

suger_list = []
while sc * SUGER_C <= LIMIT:
  while sd * SUGER_D <= LIMIT:
    suger = sc * SUGER_C + sd * SUGER_D
    if suger <= LIMIT:
      suger_list.append(suger)
    sd += 1
  sd = 0
  sc += 1

ans_suger_water = 0
ans_suger = 0

max_concentration = 0
for water in water_list:
  for suger in suger_list:
    # 砂糖水の量が0より大きく制限量以下以外の場合は次のループへ
    if not (0 < water + suger <= LIMIT):
      continue
    # 砂糖濃度計算
    suger_precent = concentration(water, suger)
    # 砂糖濃度が上限を超えていたら次のループへ
    if suger_precent > MELT_PERCENT:
      continue
    # 砂糖濃度が最高を更新かつ限界濃度を超えていなければ答えを更新
    if max_concentration < suger_precent < MELT_PERCENT:
      max_concentration = suger_precent
      ans_suger_water = water + suger
      ans_suger = suger

print(ans_suger_water, ans_suger)