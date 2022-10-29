# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

import sys

sys.stdin = open('input3.txt')

N, M = map(int, input().split())

info = [input() for i in range(N)]

maps = [[0] * M for i in range(N)]

# print(maps)

for i in range(N):
    for j in range(M):
        if info[i][j] == '1':
            maps[i][j] = 1

# print(maps)

Q = [(0,0)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

flag = 0

while flag != 1:
    now_x , now_y = Q.pop(0)
    for i in range(4):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]
        if new_y == N-1 and new_x == M-1:
            maps[new_y][new_x] = maps[now_y][now_x] + 1
            flag = 1
            break
        elif 0 <= new_x < M and 0 <= new_y < N:
            if maps[new_y][new_x] == 1:
                maps[new_y][new_x] = maps[now_y][now_x] + 1
                Q.append((new_x, new_y))
                

print(maps[N-1][M-1])