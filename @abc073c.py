N = int(input())
A = [int(input()) for _ in range(N)]

paper = []

for a in A:
  if a in paper:
    paper.remove(a)
  else:
    paper.append(a)

print(len(paper))