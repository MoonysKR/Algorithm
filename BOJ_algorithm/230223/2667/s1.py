import sys

sys.stdin = open('input7.txt')

from collections import deque

N = int(input())

maps = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    info = input()
    for j in range(N):
        maps[i][j] = int(info[j])

# print(*maps, sep='\n')
# [0, 1, 1, 0, 1, 0, 0]
# [0, 1, 1, 0, 1, 0, 1]
# [1, 1, 1, 0, 1, 0, 1]
# [0, 0, 0, 0, 1, 1, 1]
# [0, 1, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 0]
# [0, 1, 1, 1, 0, 0, 0]

result = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            cnt = 0
            que = deque()
            que.append((i, j))
            
            while que:
                # print(que)
                y, x = que.popleft()

                if maps[y][x] != 2:
                    maps[y][x] = 2
                    cnt += 1

                    dy = [-1, 0 ,1 ,0]
                    dx = [0, 1, 0, -1]

                    for k in range(4):
                        new_y = y + dy[k]
                        new_x = x + dx[k]

                        if new_y >= 0 and new_y < N and new_x >= 0 and new_x < N:
                            if maps[new_y][new_x] == 1:
                                que.append((new_y, new_x))
            
            result.append(cnt)

# print(maps)
# print(*maps, sep='\n')

print(len(result))

# result = sorted(result)
result.sort()

for i in range(len(result)):
    print(result[i])


