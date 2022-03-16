import sys

sys.stdin = open('1974_스도쿠검증_input.txt')

T = int(input())

for tc in range(1, T + 1):
    nums = [list(map(int, input().split())) for _ in range(9)]
    nums_row = nums
    nums_col = nums
    nums_sqr = nums


    # print(nums)
    # [[7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7], [8, 4, 7, 9, 3, 6, 1, 5, 2],
    #  [1, 5, 3, 8, 4, 2, 9, 7, 6], [9, 6, 2, 7, 5, 1, 8, 4, 3], [4, 2, 1, 3, 9, 8, 7, 6, 5], [3, 9, 5, 6, 7, 4, 2, 1, 8],
    #  [6, 7, 8, 2, 1, 5, 4, 3, 9]]

    # 가로 탐색
    # 각 줄 탐색
    # 1 ~ 9까지 담긴 기준 리스트 std 만들고
    # 최솟 값을 버블 정렬로 담고
    # 비교

    std = []
    for i in range(1, 10):
        std += [i]

    # print(std)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = 1
    for i in range(9):
        for j in range(8):
            for k in range(1, 9-j):
                if nums_row[i][j] > nums_row[i][j+k]:
                    nums_row[i][j], nums_row[i][j+k] = nums_row[i][j+k], nums_row[i][j]

    # print(nums)
    # [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
    #  [1, 2, 3, 4, 5, 6, 7, 8, 9]]

        if nums_row[i] != std:
            result = 0

    # 세로 탐색
    for i in range(9):
        for j in range(8):
            for k in range(1, 9-j):
                if nums_col[j][i] > nums_col[j+k][i]:
                    nums_col[j][i], nums_col[j+k][i] = nums_col[j+k][i], nums_col[j][i]
        if nums_col[i] != std:
            result = 0

    # 정방형 탐색

    for i in range(9):
        for j in range(3):
            for k in range(3):