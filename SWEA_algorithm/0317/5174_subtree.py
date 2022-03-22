import sys

sys.stdin = open('5174_subtree_input.txt')

def pre_order(n):
    global cnt
    if n != 0:
        pre_order(ch1[n])
        pre_order(ch2[n])
        cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    # E == 간선의 개수
    # N == 타겟 노드
    E, N = list(map(int, input().split()))
    info = list(map(int, input().split()))

    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)

    for i in range(int(len(info)/2)):
        if ch1[info[2*i]] == 0:
            ch1[info[2*i]] = info[2*i+1]
        else:
            ch2[info[2*i]] = info[2*i+1]

    # print(ch1, ch2)
    # [0, 6, 1, 0, 0, 3, 4][0, 0, 5, 0, 0, 0, 0]

    # 노드의 개수를 담아줄 변수
    cnt = 0

    print(f'#{tc} {pre_order(N)}')



