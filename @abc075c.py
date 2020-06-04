from functools import reduce

# judge if the list contains false. 
def is_all_true(arg):
  if isinstance(arg, bool):
    return arg
  return reduce(lambda x, y: is_all_true(x) and is_all_true(y), arg)

N, M = list(map(int, input().split()))
# list with from and to as elements.
lines_ft = []
for _ in range(M):
  _from, _to = list(map(int, input().split()))
  lines_ft.append((_from, _to))

reachable_counter = 0
# simulation of whether all the islands can be reached when each line is excluded.
for i in range(M):
  # list excluding the current line.
  verification_lines = lines_ft[:i] + lines_ft[i + 1:]
  # generated per simulation.
  is_reachable = [[False if i != j else True for i in range(N)] for j in range(N)]
  # simulate by a list that excludes one line.
  for k in range(N):
    for i in range(N):
      for j in range(N):
        is_reachable[i][j] = is_reachable[i][j] or (is_reachable[i][k] and is_reachable[k][j])
  # verify that there is an unreachable island.
  print(is_reachable)
  if is_all_true(is_reachable):
    reachable_counter += 1

print(reachable_counter)
