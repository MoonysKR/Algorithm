import sys

sys.stdin = open('5250_input.txt')

def BFS(s, cnt, visited):
    global infos, min_cnt, end, N
    if s == end:
        if cnt < min_cnt:
            min_cnt = cnt
            return

    if cnt >= min_cnt:
        return

    tmp = (N-1) * 2 - s[0] - s[1]
    if cnt + tmp >= min_cnt:
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        x = s[0] + dx[i]
        y = s[1] + dy[i]
        if 0 <= x <= N - 1 and 0 <= y <= N - 1 and visited[x][y] != 1:
            visited[x][y] = 1
            if infos[x][y] > infos[s[0]][s[1]]:
                BFS([x, y], cnt + infos[x][y] - infos[s[0]][s[1]] + 1, visited)
                visited[x][y] = 0
            else:
                BFS([x, y], cnt + 1, visited)
                visited[x][y] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    infos = [list(map(int, input().split())) for _ in range(N)]

    start = [0, 0]

    end = [N-1, N-1]

    visited = [[0] * N for _ in range(N)]

    min_cnt = 0
    for i in range(N):
        for j in range(N):
            min_cnt += infos[i][j]

    BFS(start, infos[0][0], visited)

    print(f'#{tc} {min_cnt}')