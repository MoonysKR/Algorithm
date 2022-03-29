import sys

sys.stdin = open('5189_input.txt')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    e = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    print(e)
    # [[0, 0, 0, 0],
    # [0, 0, 18, 34],
    # [0, 48, 0, 55],
    # [0, 18, 7, 0]]

    # 부분집합만들어주기
    a = 1
    for i in range(1, N):
        a *= i
    lst = [[1] for _ in range(a)]

    for i in range(a):
        while len(lst[i]) != N:
            for j in range(2, N+1):
                lst[i] += [j]
