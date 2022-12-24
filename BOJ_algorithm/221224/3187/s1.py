import sys

sys.stdin = open('input2.txt')

from collections import deque

R, C = map(int, input().split())

maps = []

for i in range(R):
    tmp = input()
    lst = []
    for j in range(C):
        lst.append(tmp[j])
    maps.append(lst)

# print(*maps, sep='\n')
# ['.', '.', '.', '#', '.', '.']
# ['.', '#', '#', 'v', '#', '.']
# ['#', 'v', '.', '#', '.', '#']
# ['#', '.', 'k', '#', '.', '#']
# ['.', '#', '#', '#', '.', '#']
# ['.', '.', '.', '#', '#', '#']

total_v = 0
total_k = 0

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'v' or maps[i][j] == 'k':
            
            if maps[i][j] == 'v':
                tmp_v = 1
                tmp_k = 0
            else:
                tmp_v = 0
                tmp_k = 1

            maps[i][j] = 'X'

            que = deque()

            que.append((i, j))

            while que:
                # print(*maps, sep='\n')
                # print(tmp_k, tmp_v)
                y, x = que.popleft()

                dy = [-1, 0, 1, 0]
                dx = [0, 1, 0, -1]

                for k in range(4):
                    new_y = y + dy[k]
                    new_x = x + dx[k]
                    if 0 <= new_y < R and 0 <= new_x < C:
                        if maps[new_y][new_x] == 'v':
                            tmp_v += 1
                            maps[new_y][new_x] = 'X'
                            que.append((new_y, new_x))
                        elif maps[new_y][new_x] == 'k':
                            tmp_k += 1
                            maps[new_y][new_x] = 'X'
                            que.append((new_y, new_x))
                        elif maps[new_y][new_x] == '.':
                            maps[new_y][new_x] = 'X'
                            que.append((new_y, new_x))
            
            if tmp_k > tmp_v:
                total_k += tmp_k
            else:
                total_v += tmp_v

# print(*maps, sep='\n')

print(total_k, total_v)