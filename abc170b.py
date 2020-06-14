X, Y = list(map(int, input().split()))

is_exist = False
for gruidaes in range(X + 1):
  turtles = X - gruidaes
  if turtles * 4 + gruidaes * 2 == Y:
    is_exist = True
    break

if is_exist:
  print('Yes')
else:
  print('No')