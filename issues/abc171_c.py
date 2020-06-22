N = int(input())

alps = 'abcdefghijklmnopqrstuvwxyz'

def cnv(X, n):
    if X//n:
        return cnv(X//n, n) + [X%n]
    return [X%n]

# ans = cnv(N, 26)
for i in range(1,28):
    ans = cnv(i-1, 26)
    print(ans, i, ''.join(list(map(lambda x: alps[x], ans))))
    # print(''.join(list(map(lambda x: alps[x - 1], ans))))
# print(''.join(list(map(lambda x: alps[x - 1], ans))))