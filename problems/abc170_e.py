from collections import defaultdict

N, Q = list(map(int, input().split()))

# child index is start from 0.
child_rate_lst = []           # idx = child, child rate
child_belong_garden_lst = []  # idx = child, child_belong_garden
# garden index is start from 1.
move_child_lst = []
destination_garden_lst = []

for _ in range(N):
  child_rate, child_belong_garden = list(map(int, input().split()))
  child_rate_lst.append(child_rate)
  child_belong_garden_lst.append(child_belong_garden)

for _ in range(Q):
  C, D = list(map(int, input().split()))
  move_child_lst.append(C - 1)
  destination_garden_lst.append(D)

# belonging children and rates from graden.
garden_child_lst = defaultdict(list)
garden_rate_lst = defaultdict(list)
for child_idx in range(N):
  # regist child index into graden_childs.
  belong_garden = child_belong_garden_lst[child_idx]
  garden_child_lst[belong_garden].append(child_idx)
  # regist child_rate into garden_rates.
  child_rate = child_rate_lst[child_idx]
  garden_rate_lst[belong_garden].append(child_rate)


for i in range(Q):
  # move child to destination garden.
  move_child = move_child_lst[i]
  destination_garden = destination_garden[i]
  child_belong_garden_lst[move_child] = destination_garden
