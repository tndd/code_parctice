sx, sy, tx, ty = list(map(int, input().split()))

def get_path(moves):
  path = ''
  for y, x in moves:
    if y > 0:
      path += 'U' * y
    else:
      path += 'D' * -y
    if x > 0:
      path += 'R' * x
    else:
      path += 'L' * -x
  return path

first_moves = []
foward_y = ty - sy
foward_x = tx - sx
first_moves.append((foward_y, foward_x))
first_moves.append((-foward_y, -foward_x))

second_moves = []
foward_y = (ty + 1) - sy
foward_x = tx - (sx - 1)
second_moves.append((0, -1))
second_moves.append((foward_y, foward_x))
second_moves.append((-1, 0))
second_moves.append((0, 1))
second_moves.append((-foward_y, -foward_x))
second_moves.append((1, 0))

print(get_path(first_moves + second_moves))