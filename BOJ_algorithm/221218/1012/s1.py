import sys

sys.stdin = open('input2.txt')

# 문제 풀이 법
# 1. 농장에서 1탐색하는데
# 2. 1을 만나면 visited체크, 멈추고
# 3. BFS 돌아주는 함수 실행
    # 3-1. BFS를 하면서 visited 처리
# 4. 다음 1 탐색

from collections import deque

# BFS 함수
def bfs(x, y):
    global visited, farm

    que = deque()

    que.append((x, y))

    while que:
        now_x, now_y = que.popleft()
        
        visited[now_y][now_x] = 1
        
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            if 0 <= new_x < M and 0 <= new_y < N:
                if farm[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                    visited[new_y][new_x] = 1
                    que.append((new_x, new_y))

T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    # print(N, M, K)

    farm = [[0] * M for _ in range(N)]

    # print(farm)
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 
    
    for i in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = 1

    # print(farm)
    # [
    # [0, 0, 0, 0, 1], 
    # [0, 0, 0, 0, 0], 
    # [1, 1, 1, 1, 1]
    # ]

    visited = [[0] * M for _ in range(N)]


    result = 0

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and visited[i][j] == 0:
                bfs(j, i)
                result += 1

    print(result)


