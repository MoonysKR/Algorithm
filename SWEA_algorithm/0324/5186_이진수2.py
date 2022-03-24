import sys

sys.stdin = open('5186_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    # print(N)
    # 0.625
    # 소수점은 2**i를 더한 값들의 연속, 빼줘야겠다

    result = ''  # 결과 담을 문자열 변수
    i = -1  # 2의 2진수, while문이 돌 때마다 1씩 감소할 예정
    while N != 0:
        if len(result) == 13:
            result = 'overflow'
            break
        else:
            if N >= 2 ** i:  # N이 2의 i제곱 보다 크다면 빼주고, 해당 소수점은 1
                N = N - 2 ** i
                i -= 1
                result += '1'
            else:  # N이 2의 i 제곱보다 작다면 해당 소수점은 0
                result += '0'
                i -= 1

    print(f'#{tc} {result}')

