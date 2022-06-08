import sys

sys.stdin = open('1970_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    a = 0
    if N >= 50000:
        a = N // 50000
        N -= a * 50000

    b = 0
    if 10000 <= N < 50000:
        b = N // 10000
        N -= b * 10000

    c = 0
    if 5000 <= N < 10000:
        c = N // 5000
        N -= c * 5000

    d = 0
    if 1000 <= N < 5000:
        d = N // 1000
        N -= d * 1000

    e = 0
    if 500 <= N < 1000:
        e = N // 500
        N -= e * 500

    f = 0
    if 100 <= N < 500:
        f = N // 100
        N -= f * 100

    g = 0
    if 50 <= N < 100:
        g = N // 50
        N -= g * 50

    h = 0
    if 10 <= N < 50:
        h = N // 10
        N -= h * 10

    result = [a, b, c, d, e, f, g, h]
    print(f'#{tc}')
    print(*result)