N, M, Q = list(map(int, input().split()))
pkgs = []
for i in range(N):
    _w, _v = list(map(int, input().split()))
    pkgs.append({'w': _w, 'v': _v})
boxes = list(map(int, input().split()))
r = []
l = []
for i in range(Q):
    _l, _r = list(map(int, input().split()))
    r.append(_r)
    l.append(_l)

# sort the package in descending order of value.
pkgs = sorted(pkgs, key=lambda x: x['v'], reverse=True)
# sort the boxes in descending order of capacity.
boxes = sorted(boxes, reverse=True)
for i in range(Q):
    value = 0
    pkgs_per_q = pkgs[:]
    # removing the boxes between l and r
    boxes_lr = boxes[:l[i]-1] + boxes[r[i]:]
    for box_vol in boxes_lr:
        for i, pkg in enumerate(pkgs_per_q):
            if pkg['w'] <= box_vol:
                value += pkg['v']
                pkgs_per_q.pop(i)
    print(value)
