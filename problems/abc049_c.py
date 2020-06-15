S = input()

TEXTS = ['dream', 'dreamer', 'erase', 'eraser']

is_updated = True
while is_updated and len(S) > 0:
  is_updated = False
  for text in TEXTS:
    if S[len(S) - len(text):] == text:
      S = S[:len(S) - len(text)]
      is_updated = True

if S == '':
  print('YES')
else:
  print('NO')