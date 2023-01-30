import sys

sys.stdin = open('input5.txt')

M, N = map(int, input().split())

from collections import deque

maps = [list(map(int, input().split())) for _ in range(N)]

# print(*maps, sep='\n')
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1]

que = deque()

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:
            que.append((i, j, 0))

max_day = 0

while que:
    # print(que)
    y, x, day = que.popleft()

    if day > max_day:
        max_day = day

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        # print(new_y, new_x)

        if new_y >= 0 and new_y <= N - 1 and new_x >= 0 and new_x <= M - 1:
            if maps[new_y][new_x] == 0:
                maps[new_y][new_x] = 1
                que.append((new_y, new_x, day + 1))

# print(*maps, sep='\n')

flag = 0
result = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            flag = 1
            result = -1

if flag == 0:
    result = max_day

print(result)