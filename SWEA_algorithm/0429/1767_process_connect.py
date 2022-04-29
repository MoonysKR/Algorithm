import sys

sys.stdin = open('1767_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    # 전략
    # 1. 코어를 탐색하고
    # 2. 해당 코어에서 여러 방향으로 전력 연결 후 다음 재귀호출
    # 4. 최소 전선 수 구할 min_lines
    # 3. 최대 코어 수 구할 max_elecs

    min_lines = N * N
    max_elecs = 0

    def dfs(visited):
        for i in range(N):
            for j in range(N):
                if infos[i][j] == 1 and visited[i][j] == 0:
                    visited[i][j] = 1
                    start = [i, j]

        # start에서 상하 좌우로 전선을 연결 할 수 있으면 연결해주고 dfs 다시 실행
        # 상
        if 0 < start[0]:
            for i in range(start[0]):
                if visited[i][start[1]] != 0:
                    for j in range(i+1, start[0]):
                        visited[i][start[1]] = 0
                    break
                else:
                    visited[i][start[1]] = 2
            dfs(visited)
            # visited 초기화 해주기
            for i in range

        # 하
        if start[0] < N - 1:
            for i in range(start[0] + 1, N):
                if
