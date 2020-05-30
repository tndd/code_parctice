def concentration(water, suger):
  return 100 * suger / (water + suger)

WATER_A, WATER_B, SUGER_C, SUGER_D, MELT_AMOUNT, LIMIT = map(int, input().split())

WATER_A *= 100
WATER_B *= 100

max_concentration = 0
ans_suger_water = 0
ans_suger = 0

for wa in range(31):
  for wb in range(31):
    for sc in range(31):
      for sd in range(31):
        water = WATER_A * wa + WATER_B * wb
        suger = SUGER_C * sc + SUGER_D * sd
        if 0 < water + suger <= LIMIT:
          percent = concentration(water, suger)
          if max_concentration < percent <= MELT_AMOUNT:
            max_concentration = percent
            ans_suger_water = water + suger
            ans_suger = suger

print(ans_suger_water, ans_suger)