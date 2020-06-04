N, M = list(map(int, input().split()))
# list with from and to as elements.
lines_ft = []
for _ in range(M):
  _from, _to = list(map(int, input().split()))
  lines_ft.append(_from, _to)

reachable_counter = 0
# simulation of whether all the islands can be reached when each line is excluded.
for i in range(M):
  # list excluding the current line.
  verification_lines = lines_ft[:i] + lines_ft[i + 1:]
  # generated per simulation.
  is_reached_islands = [False for _ in range(N)]
  is_reached_islands[0] = True
  # simulate by a list that excludes one line.
  for line in lines_ft:
    # TODO implement Warshall–Floyd Algorithm?
    pass