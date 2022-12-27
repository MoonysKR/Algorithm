import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    result = 1

    for i in range(N):
        result = result * (M - i)

    print(result)
            