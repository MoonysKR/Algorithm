import sys

sys.stdin = open('1954_달팽이숫자_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]

    # 첫 줄 채워주기
    for n in range(1, N+1):
        snail[0][n-1] = [n]

    # 다음부터는 N이 1씩 줄어든 숫자 길이로 두번 씩 들어감
    # 순회하는 횟수는 N-1 => for문으로 0~N-1 순회
    # 0이나 짝수일 때는 밑 => 왼쪽
    # 홀수 일 때는 위 => 오른쪽
    # 위치는 [0, N-1]
    # 숫자는 N

    pos = [0, N-1]
    num = N
    for n in range(N-1):
        if n % 2 == 0:
            for m in range(N-n-1):

