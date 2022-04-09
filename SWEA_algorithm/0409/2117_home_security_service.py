import sys

sys.stdin = open('2117_input.txt')

T = int(input())

for tc in range(1, T + 1):
    # N == 도시크기 / M == 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(N)]

    max_profit = -1 * ((2*N-1)**2+(2*N-2)**2)

    home_cnt = 0
    for i in range(N):
        for j in range(N):
            if infos[i][j] == 1:
                home_cnt += 1

    k = 1  # 함수에 k를 넣고, 증가시키면서 최적의 k를 산출할 예정

    def find(k):
        global N, M, max_profit

        cost = k * k + (k-1) * (k-1)

        if k == N + N - 1:
            profit = home_cnt * M - cost
            if profit > max_profit:
                max_profit = profit

        else:
            for i in range(N):
                for j in range(N):