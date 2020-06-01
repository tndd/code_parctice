Sd = input()
T = input()

Sdl = len(Sd)
Tl = len(T)

ans_str = ''

# inspect strings in reverse order
for i in reversed(range(Sdl - Tl + 1)):
  # if there is a character that hits, compare it with the string T.
  if Sd[i] == T[0] or Sd[i] == '?':
    is_match = True
    # loop for length of string T
    for j in range(Tl):
      # if string Sd doesn't match T and is not '?'
      if Sd[i + j] != T[j] and Sd[i + j] != '?':
        is_match = False
        break
    # if there is a T that meets the conditions, replace part of Sd
    if is_match:
      ans_str = Sd[:i] + T + Sd[i + Tl:]
      break

if ans_str:
  print(ans_str.replace('?', 'a'))
else:
  print('UNRESTORABLE')