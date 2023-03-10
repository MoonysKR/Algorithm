import sys

sys.stdin = open('input1.txt')

from collections import deque

N, M = map(int, input().split())

maps = []

for i in range(N):
    tmp_lst = []
    tmp_map = input()
    for j in range(M):
        if tmp_map[j] == 'W':
            tmp_lst.append(0)
        else:
            tmp_lst.append(1)
    maps.append(tmp_lst)

# print(*maps, sep='\n')
# [0, 1, 1, 0, 0, 0, 1]
# [1, 1, 1, 0, 1, 1, 1]
# [1, 0, 1, 0, 1, 0, 0]
# [1, 0, 1, 0, 1, 1, 1]
# [0, 1, 1, 0, 1, 0, 0]

max_length = 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 1:

            visited = [[0] * M for _ in range(N)]

            visited[i][j] = 1

            togo = deque()

            togo.append((i, j, 0))

            while togo:
                y, x, cnt = togo.popleft()

                if cnt > max_length:
                    max_length = cnt

                dy = [-1, 0, 1, 0]
                dx = [0, 1, 0, -1]

                for k in range(4):
                    new_y = y + dy[k]
                    new_x = x + dx[k]

                    if new_y >= 0 and new_y <= N - 1 and new_x >= 0 and new_x <= M - 1:
                        if maps[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                            visited[new_y][new_x] = 1
                            togo.append((new_y, new_x, cnt + 1))

print(max_length)