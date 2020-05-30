def concentration(water, suger):
  return 100 * suger / (water + suger)

WATER_A, WATER_B, SUGER_C, SUGER_D, MELT_AMOUNT, LIMIT = map(int, input().split())

WATER_A *= 100
WATER_B *= 100

max_concentration = 0
ans_suger_water = 0
ans_suger = 0

wa = wb = sc = sd = 0

while wa * WATER_A <= LIMIT:
  while wb * WATER_B <= LIMIT:
    while sc * SUGER_C <= LIMIT:
      while sd * SUGER_D <= LIMIT:
        water = WATER_A * wa + WATER_B * wb
        suger = SUGER_C * sc + SUGER_D * sd
        if 0 < water + suger <= LIMIT:
          percent = concentration(water, suger)
          if max_concentration < percent <= MELT_AMOUNT:
            max_concentration = percent
            ans_suger_water = water + suger
            ans_suger = suger
        sd += 1
      sc += 1
    wb += 1
  wa += 1

print(ans_suger_water, ans_suger)