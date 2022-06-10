import sys

sys.stdin = open('1959_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if len(A) >= len(B):
        max_num = 0
        for i in range(len(B)):
            max_num += A[i] * B[i]

        for i in range(len(A) - len(B) + 1):
            tmp = 0
            for j in range(len(B)):
                tmp += A[i+j] * B[j]
            if tmp > max_num:
                max_num = tmp
    else:
        max_num = 0
        for i in range(len(A)):
            max_num += A[i] * B[i]

        for i in range(len(B) - len(A) + 1):
            tmp = 0
            for j in range(len(A)):
                tmp += B[i + j] * A[j]
            if tmp > max_num:
                max_num = tmp

    print(f'#{tc} {max_num}')