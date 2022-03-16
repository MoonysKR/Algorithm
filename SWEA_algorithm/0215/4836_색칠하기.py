import sys

sys.stdin = open('4836_색칠하기_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]

    # 빈 공간 추가
    space = [[0]*10 for _ in range(10)]

    # if문으로 Red 식별 후, 빈공간에 1 할당
    # Blue 식별 후, 공간에 2 더함
    # 최종적으로 Purple 구역은 3이 나옴
    for i in range(N):
        if info[i][4] == 1:
            for j in range(info[i][0]-1, info[i][2]):
                for k in range(info[i][1]-1, info[i][3]):
                    space[j][k] += 1
        else:
            for j in range(info[i][0]-1, info[i][2]):
                for k in range(info[i][1]-1, info[i][3]):
                    space[j][k] += 2

    # Purple 개수 구하기
    purple = 0
    for i in range(10):
        for j in range(10):
            if space[i][j] == 3:
                purple += 1

    print(f'#{tc} {purple}')

