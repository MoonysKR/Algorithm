import sys

sys.stdin = open('4366_input.txt')

import copy

T = int(input())

for tc in range(1,  T+1):

    # 2진수 == N
    # 3진수 == M
    N = input()
    M = input()

    A = []
    for i in range(len(N)):
        A += N[i]

    B = []
    for i in range(len(M)):
        B += M[i]

    i = -1
    flag = 0
    while flag == 0:
        tmp_A = copy.deepcopy(A)
        tmp_B = copy.deepcopy(B)
        for j in range(2):
            tmp_A[i] = str(j)
            tmp_N = ''
            for k in range(len(tmp_A)):
                tmp_N += tmp_A[k]
            for l in range(3):
                tmp_B[i] = str(l)
                tmp_M = ''
                for m in range(len(tmp_B)):
                    tmp_M += tmp_B[m]
                if int(tmp_N, 2) == int(tmp_M, 3):
                    A[i], B[i] = j, l
                    flag = 1
                    print(f'#{tc} {int(tmp_N, 2)}')
        i -= 1



