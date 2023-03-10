import sys

sys.stdin = open('input2.txt')

from collections import deque

N = int(input())

maps = list(list(map(int, input().split())) for _ in range(N))

# print(*maps, sep='\n')
# [6, 8, 2, 6, 2]
# [3, 2, 3, 4, 6]
# [6, 7, 3, 3, 2]
# [7, 2, 5, 3, 6]
# [8, 9, 5, 2, 7]

max_height = 1
min_height = 100

for i in range(N):
    for j in range(N):
        if maps[i][j] > max_height:
            max_height = maps[i][j]
        if maps[i][j] < min_height:
            min_height = maps[i][j]

max_groups = 0

for rain in range(min_height, max_height + 1):

    saves = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maps[i][j] >= rain:
                saves[i][j] = 1

    groups = 0

    for i in range(N):
        for j in range(N):
            if saves[i][j] == 1 and visited[i][j] == 0:
                
                tocheck = deque()

                tocheck.append((i, j))

                while tocheck:
                    y, x = tocheck.popleft()

                    dy = [-1, 0, 1, 0]
                    dx = [0, 1, 0, -1]

                    for k in range(4):
                        new_y = y + dy[k]
                        new_x = x + dx[k]

                        if new_y >= 0 and new_y <= N - 1 and new_x >= 0 and new_x <= N - 1:
                            if visited[new_y][new_x] == 0 and saves[new_y][new_x] == 1:
                                visited[new_y][new_x] = 1
                                tocheck.append((new_y, new_x))
                
                groups += 1
    
    if groups > max_groups:
        max_groups = groups

print(max_groups)
