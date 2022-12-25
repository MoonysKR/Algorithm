import sys

sys.stdin = open('input4.txt')

from collections import deque

N = int (input())

maps = [list(map(int, input().split())) for _ in range (N)]

# print(*maps, sep='\n')
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

# 파이프 - \ | , 각각 2 3 4

maps[0][1] = 2

ways = 0

que = deque()

# y, x, z 각각 좌표 및 파이프 모양

que.append((0, 1, 2))

while que:
    # print(que)
    y, x, z = que.popleft()

    dy = [0, 1, 1]
    dx = [1, 1, 0]

    l_y = y + dy[0]
    l_x = x + dx[0]

    ld_y = y + dy[1]
    ld_x = x + dx[1]

    d_y = y + dy[2]
    d_x = x + dx[2]

    if y == N - 1 and x == N - 1:
        ways += 1

    elif z == 2:
        if l_x < N:
            if maps[l_y][l_x] == 0:
                que.append((l_y, l_x, 2))

        if l_x < N and d_y < N:
            if maps[l_y][l_x] == 0 and maps[ld_y][ld_x] == 0 and maps[d_y][d_x] == 0:
                que.append((ld_y, ld_x, 3))

    elif z == 3:
        if l_x < N:
            if maps[l_y][l_x] == 0:
                que.append((l_y, l_x, 2))

        if l_x < N and d_y < N:
            if maps[l_y][l_x] == 0 and maps[ld_y][ld_x] == 0 and maps[d_y][d_x] == 0:
                que.append((ld_y, ld_x, 3))

        if d_y < N:
            if maps[d_y][d_x] == 0:
                que.append((d_y, d_x, 4))

    elif z == 4:
        if l_x < N and d_y < N:
            if maps[l_y][l_x] == 0 and maps[ld_y][ld_x] == 0 and maps[d_y][d_x] == 0:
                que.append((ld_y, ld_x, 3))

        if d_y < N:
            if maps[d_y][d_x] == 0:
                que.append((d_y, d_x, 4))

print(ways)