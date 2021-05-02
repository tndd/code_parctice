from collections import deque
import numpy as np

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 0

for y in range(H):
    for x in range(W):
        # skip if the starting point is the wall.
        if S[y][x] == "#":
            continue
        # distance from the starting point.
        dist = [[0] * W for _ in range(H)]
        # the queue of the next point to be searched.
        queue = deque([(y, x)])
        while queue:
            now_y, now_x = queue.popleft()
            for i, j in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                next_y, next_x = now_y + i, now_x + j
                # if next yx is outrange, continue.
                if next_y < 0 or H <= next_y or next_x < 0 or W <= next_x:
                    continue
                # overwrite deistane if the point is unexplored location.
                if S[next_y][next_x] != '#' and dist[next_y][next_x] == 0:
                    dist[next_y][next_x] = dist[now_y][now_x] + 1
                    # add the next search point to queue.
                    queue.append((next_y, next_x))
        dist[y][x] = 0
        # find the maximum distance.
        ans = max(ans, np.max(dist))

print(ans)
