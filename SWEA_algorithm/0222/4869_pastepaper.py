import sys

sys.stdin = open('4869_pastepaper_input.txt')

def paste_paper(N):
    if N == 20:  # 20일 때 경우의 수 3가지
        return 3
    if N == 10:  # 10일 때 경우의 수 1가지
        return 1
    else:
        return paste_paper(N-10) + paste_paper(N-20) * 2
        # 가로가 50일 경우의 경우의 수 =
        # 40의 경우의수 * 1(10을 제거하는 것은 경우의 수 한가지) + 30의 경우의수 * 2 (20을 제거한 경우의 수 3가지인데 10을제거할 때와 겹치는 상황이 있어서 2)


T = int(input())

for tc in range(1, 4):
    N = int(input())

    print(f'#{tc} {paste_paper(N)}')