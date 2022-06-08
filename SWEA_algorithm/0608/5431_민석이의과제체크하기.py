import sys

sys.stdin = open('5431_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    info = list(map(int, input().split()))

    results = []

    for i in range(1, N+1):
        if i not in info:
            results += [i]

    print(f'#{tc}', end=' ')
    print(*results)