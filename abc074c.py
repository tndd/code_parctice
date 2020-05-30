def concentration(water, suger):
  return 100 * suger / (water + suger)

WATER_A, WATER_B, SUGER_C, SUGER_D, MELT_AMOUNT, LIMIT = map(int, input().split())

max_concentration = 0
ans_suger_water = 0
ans_suger = 0

for wa in range(WATER_A + 1):
  for wb in range(WATER_B + 1):
    for sc in range(SUGER_C + 1):
      for sd in range(SUGER_D + 1):
        water = (wa + wb) * 100
        suger = sc + sd
        if 0 < water + suger <= LIMIT:
          percent = concentration(water, suger)
          if max_concentration < percent <= MELT_AMOUNT:
            print(percent)
            max_concentration = percent
            ans_suger_water = water + suger
            ans_suger = suger

print(ans_suger_water, suger)