import sys

sys.stdin = open('5105_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]


    # 시작점과 끝점 찾기기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_y, start_x = i, j
            if maze[i][j] == 3:
                goal_y, goal_x = i, j
    visited = [[0]*N for _ in range(N)]

    que = deque([[start_y, start_x]])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[start_y][start_x] = 1

    while que:
        y, x = que.popleft()
        for i in range(4):
            new_y = y + dx[i]
            new_x = x + dy[i]
            if 0 <= new_y < N and 0 <= new_x < N:
                if visited[new_y][new_x] == 0:
                    if maze[new_y][new_x] == 0:
                        visited[new_y][new_x] = visited[y][x] + 1
                        que.append([new_y, new_x])
                    if maze[new_y][new_x] == 3:
                        visited[new_y][new_x] = visited[y][x] - 1
                        break

    print(f'#{tc} {visited[goal_y][goal_x]}')