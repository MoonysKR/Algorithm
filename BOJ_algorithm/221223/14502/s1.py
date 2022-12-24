import sys

sys.stdin = open('input3.txt')

from collections import deque

# 벽을 세우는 함수
    # 3개일때와 그렇지 않을 때를 나누어 사용
def set_walls(walls, maps):
    global visited


    if walls == 3:  # 세 개일 때는 개수 구하고 최대값인지 비교하는 함수 실행
        get_safes(maps)

    elif walls == 0:  # 0개에서는 벽 추가하고 다음으로 토스
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    set_walls(walls+1, maps)
                    maps[i][j] = 0
    
    else:  # 한 개이거나 두 개라면 방문했던데인가 파악 후 방문하지 않은 곳이라면 세번째로 토스
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    set_walls(walls+1, maps)
                    # if maps not in visited:
                    #     set_walls(walls+1, maps)
                    #     visited.append(maps)
                    maps[i][j] = 0


# 세이프룸의 개수를 세우는 함수
def get_safes(maps):
    global max_safes, N, M

    tmp = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if maps[i][j] !=0:
                tmp[i][j] = maps[i][j]

    # 바이러스 전염 BFS로 인접한 0 모두 2로 처리
    virus = deque()

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                virus.append((i, j))
    
    while virus:
        y, x = virus.popleft()

        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if 0 <= new_y < N and 0 <= new_x < M:
                if tmp[new_y][new_x] == 0:
                    tmp[new_y][new_x] = 2
                    virus.append((new_y, new_x))
    
    # 남아 있는 0의 개수 확인
    cnt = 0

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    
    if cnt > max_safes:
        max_safes = cnt

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# print(*maps, sep='\n')
# [2, 0, 0, 0, 1, 1, 0]
# [0, 0, 1, 0, 1, 2, 0]
# [0, 1, 1, 0, 1, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 1, 1]
# [0, 1, 0, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0]

walls = 0

visited = []  # 개수를 세기 전에 벽의 위치를 파악하는 용도 , 2개를 세우고 3개에 보내기 전에 파악할 예정

max_safes = 0

set_walls(walls, maps)

print(max_safes)


# visited 처리를 못함 ㅠㅠㅠㅠ