import sys

sys.stdin = open('5248_input.txt')


# def check(num):
#     global group
#     if group[num] == num:
#         return
#
#     if group[group[num]] == group[num]:
#         return
#
#     if group[group[num]] != group[num]:
#         group[num] = group[group[num]]
#         check(group[num])
#         check(num)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)
    # [1, 2, 3, 4]

    groups = []

    for i in range(0, N+1):
        groups += [[i]]
    # print(groups)
    # [[0], [1], [2], [3], [4], [5]]

    for i in range(M):
        for j in range(N+1):
            if arr[2*i] in groups[j]:
                for k in range(N+1):
                    if arr[2*i+1] in groups[k]:
                        if groups[j] != groups[k]:
                            groups[j] += groups[k]
                            groups[k] = []
                            # print(groups)
    # print(groups)
    # [[0], [1, 2], [], [3, 4], [], [5]]

    cnt = -1
    for group in groups:
        if len(group) > 0:
            cnt += 1
    print(f'#{tc} {cnt}')

    # group = []
    # for i in range(0, N+1):
    #     group += [i]
    # # print(group)
    # # [0, 1, 2, 3, 4, 5, 6, 7]
    #
    # for i in range(0, len(arr), 2):
    #     group[arr[i+1]] = arr[i]
    # print(group)
    # # [0, 1, 2, 2, 7, 4, 4, 7]
    #
    # for i in range(1, N+1):
    #     check(i)
    # print(group)
    # # [0, 1, 2, 2, 7, 7, 7, 7]
    #
    # tmp = []
    # for i in range(N+1):
    #     if group[i] not in tmp:
    #         tmp += [group[i]]
    # print(tmp)
    # # [0, 1, 2, 7]
    # result = len(tmp) - 1
    #
    # print(f'#{tc} {result}')
    # # #3 3
    #


