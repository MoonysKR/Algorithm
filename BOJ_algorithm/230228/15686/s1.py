import sys
sys.stdin = open('input2.txt')

from collections import deque


def get_stores(bit, cnt, start):
    global cases, stores, M
    print(bit)

    if cnt == M:
        lst = []
        for i in range(len(bit)):
            if bit[i] == 1:
                lst.append((stores[i]))
        cases.append(lst)
    
    else:
        for i in range(start, len(bit) - M + 1 + cnt):
            if bit[i] == 0:
                bit[i] = 1
                get_stores(bit, cnt + 1, i + 1)
                bit[i] = 0


def check(case, maps):
    global N, result

    for i in range(M):
        y, x = case[i]
        maps[y][x] = 3

    tmp = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                que = deque()
                que.append((i, j, 0))

                visited = [[0 for _ in range(N)] for _ in range(N)]

                min_distance = N * N * N * N

                while que:

                    if min_distance != N * N * N * N:
                        if min_distance > result:
                            break

                    y, x, distance = que.popleft()

                    dy = [-1, 0, 1, 0]
                    dx = [0, 1, 0, -1]

                    for k in range(4):
                        new_y = y + dy[k]
                        new_x = x + dx[k]

                        if new_y >= 0 and new_y <= N - 1 and new_x >= 0 and new_x <= N - 1:
                            if visited[new_y][new_x] == 0:
                                visited[new_y][new_x] = 1
                                if maps[new_y][new_x] == 0 or maps[new_y][new_x] == 1 or maps[new_y][new_x] == 2:
                                    que.append((new_y, new_x, distance + 1))
                                else:
                                    if distance + 1 < min_distance:
                                        min_distance = distance + 1

                tmp += min_distance
    
    if result == 0:
        result = tmp
        # print(tmp, case, maps)
    else:
        if tmp < result:
            result = tmp
            # print(tmp, case, maps)
    
    for i in range(M):
        y, x = case[i]
        maps[y][x] = 2

N, M = map(int, input().split())

maps = list(list(map(int, input().split())) for _ in range(N))

stores = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            stores.append((i, j))

# print(stores)

bit = [0] * len(stores)

# print(bit)

cases = []

get_stores(bit, 0, 0)

# print(cases)
# [[(0, 1), (3, 0)], [(0, 1), (4, 0)], [(0, 1), (4, 1)], [(0, 1), (4, 4)], [(3, 0), (4, 0)], [(3, 0), (4, 1)], [(3, 0), (4, 4)], [(4, 0), (4, 1)], [(4, 0), (4, 4)], [(4, 1), (4, 4)]] 

result = 0


for case in cases:
    check(case, maps)

print(result)