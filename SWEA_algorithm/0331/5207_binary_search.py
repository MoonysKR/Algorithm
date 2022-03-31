import sys

sys.stdin = open('5207_input.txt')

import copy


def search(arr):
    global i, cnt, B, A
    tmp = copy.deepcopy(arr)
    # print(tmp, i)
    if i <= M - 1:
        middle = B[i]
        # print(middle)
        if tmp[len(tmp) // 2] == middle:
            i += 1
            cnt += 1
            return search(A)
        elif tmp[len(tmp) // 2] < middle and len(tmp) > 1:
            # print(i, tmp[len(tmp)//2+1:])
            return search(tmp[len(tmp) // 2 :])
        elif tmp[len(tmp) // 2] > middle and len(tmp) > 1:
            # print(i, tmp[:len(tmp)//2+1])
            if len(tmp) == 2:
                return search(tmp[: len(tmp) // 2])
            else:
                return search(tmp[: len(tmp) // 2 + 1])
        else:
            i += 1
            # print('i', i)
            return search(A)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    i = 0

    search(A)
    print(f'#{tc} {cnt}')
