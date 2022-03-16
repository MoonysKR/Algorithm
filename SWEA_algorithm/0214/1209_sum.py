import sys

sys.stdin = open('0214_sum_input.txt')

for tc in range(1,11):

    N = int(input())
    num_lists = [list(map(int, input().split())) for _ in range(100)]

    # 가로 합 리스트 구하기
    row_sums = []
    for r in range(100):
        row_total = 0
        for n in range(100):
            row_total += num_lists[r][n]
        row_sums += [row_total]

    # 세로 합 리스트 구하기
    column_sums = []
    for r in range(100):
        column_total = 0
        for n in range(100):
            column_total += num_lists[n][r]
        column_sums += [column_total]

    # 대각선(L -> R) 합 구하기
    slash_sums = []
    for r in range(100):
        slash_total_lr = 0
        for n in range(100):
            if r == n:
                slash_total_lr += num_lists[r][n]
    slash_sums = [slash_total_lr]

    # 대각선(R -> L) 합 구하기
    for r in range(100):
        slash_total_rl = 0
        for n in range(100):
            if r + n == 99:
                slash_total_rl += num_lists[r][n]
    slash_sums += [slash_total_rl]

    # 전체 리스트 만들기
    totals = row_sums + column_sums + slash_sums

    # 최댓값 구하기
    max_total = 0
    for total in totals:
        if total > max_total:
            max_total = total

    print(f'#{tc} {max_total}')