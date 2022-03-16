import sys

sys.stdin = open('4881_arrayminsum_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dup = arr
    sums = []
    tmp = 0
    loc = []
    for i in range(N):
        for j in range(N):
            if dup[i][j] != 0:
                tmp += dup[i][j]
                loc += [[i, j]]
                for k in range(N):
                    dup[i][k] = 0
                    dup[k][j] = 0
            else:
                tmp += dup[i][j]
        arr
    sums += [tmp]
    print(sums)
    min_sum = sums[0]
    for l in range(len(sums)):
        if sums[l] < min_sum:
            min_sum = sums[l]

    print(f'#{tc} {min_sum}')