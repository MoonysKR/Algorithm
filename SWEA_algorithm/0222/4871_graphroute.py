import sys

sys.stdin = open('4871_graphroute_input.txt')


def rte(S, G):
    global V, E, data, visited, limit, tc
    if S == G:
        print(f'#{tc} 1')
    else:
        visited[S] = 1
        for i in range(V + 1):
            if data[S][i] == 1 and visited[i] == 0:
                rte(i, G)

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    data = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        data[infos[i][0]][infos[i][1]] = 1

    # print(data)
    # [[0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 1, 1, 0, 0],
    # [0, 0, 0, 1, 0, 1, 0],
    # [0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 1],
    # [0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0]]

    visited = [0] * (V+1)

    limit = 0

    rte(S, G)