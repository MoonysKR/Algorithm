import sys

sys.stdin = open('input1.txt')

# 상하좌우 대각선 변화
def convert(y, x, maps):
    
    # y, x 축 1로 변환
    for i in range(N):
        if maps[i][x] == 0:
            maps[i][x] = 1
        if maps[y][i] == 0:
            maps[y][i] = 1
    
    for i in range(1, N):
        if y + i < N and x + i < N:
            if maps[y + i][x + i] == 0:
                maps[y + i][x + i] = 1
        if y - i >= 0 and x - i >= 0:
            if maps[y - i][x - i] == 0:
                maps[y - i][x - i] = 1
        if y + i < N and x - i >= 0:
            if maps[y + i][x - i] == 0:
                maps[y + i][x - i] = 1
        if y - i >= 0 and x + i < N:
            if maps[y - i][x + i] == 0:
                maps[y - i][x + i] = 1


# 개수를 구하는 함수
def get_queens(queens):
    global N, cnt

    if len(queens) == N:
        cnt += 1
        return

    if queens[-1][0] == N - 1:
        return

    maps = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(queens)):
        maps[queens[i][0]][queens[i][1]] = 2
        convert(queens[i][0], queens[i][1], maps)
    
    for i in range(queens[-1][0] + 1, N):
        for j in range(N):
            if maps[i][j] == 0:
                get_queens(queens + [(i, j)])            

N = int(input())

cnt = 0

for j in range(N):
    get_queens([(0, j)])

print(cnt)