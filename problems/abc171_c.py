N = int(input())

alps = 'abcdefghijklmnopqrstuvwxyz'

def cnv(X, n):
    if X//n:
        return cnv(X//n, n) + [X%n]
    return [X%n]

ans = cnv(N, 26)
print(''.join(list(map(lambda x: alps[x - 1], ans))))