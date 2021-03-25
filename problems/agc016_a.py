S = input()

cnt_min = float('inf')
chars = set(S)

for c in chars:
    sl = list(S)
    cnt = 0
    i = 0
    while True:
        if sl.count(c) == len(sl):
            cnt_min = min(cnt_min, cnt)
            break
        elif len(sl) == 1:
            break
        for i in range(len(sl) - 1):
            if sl[i] != c:
                sl[i] = sl[i + 1]
        cnt += 1
        sl.pop(-1)

print(cnt_min)
