import sys

sys.stdin = open('5188_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    S = [0, 0]

    # 좌, 하 이동만
    dx = [1, 0]
    dy = [0, 1]

    q = deque([S])

    # 방문했을 때의 최소값을 담아줄 2차원 배열
    visited = [[0] * N for _ in range(N)]

    # 시작지점 위치 담아주기
    visited[S[0]][S[1]] = infos[S[0]][S[1]]

    # 목표 값없이 전부 순회
    while q:
        a, b = q.popleft()
        for i in range(2):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < N:
                # 방문할 위치의 값이 0이라면, 아직 한번도 순회를 안했다면 그냥 담아주기
                if visited[x][y] == 0:
                    visited[x][y] = visited[a][b] + infos[x][y]
                    q.append([x, y])
                # 방문할 위치의 값이 0 이 아니고 기존값보다 들어오는 값이 더 작다면, 담아주기
                elif visited[x][y] != 0 and visited[a][b] + infos[x][y] < visited[x][y]:
                    visited[x][y] = visited[a][b] + infos[x][y]
                    q.append([x, y])

    print(f'#{tc} {visited[N-1][N-1]}')

