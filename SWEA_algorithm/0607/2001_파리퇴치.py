import sys

sys.stdin = open('2001_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    # print(info)

    max_kill = 0

    tmp_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for l in range(M):
                    tmp_kill += info[i+k][j+l]
            if tmp_kill > max_kill:
                max_kill = tmp_kill
            tmp_kill = 0

    print(f'#{tc} {max_kill}')

