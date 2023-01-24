import sys

sys.stdin = open('input5.txt')

def min_rgb(nums, before, cost):
    global N, info, min_cost

    if nums == N:
        if cost < min_cost:
            min_cost = cost

    if nums == 0:
        for i in range(3):
            if i == 0:
                min_rgb(nums + 1, 'R', cost + info[nums][i])
            elif i == 1:
                min_rgb(nums + 1, 'G', cost + info[nums][i])
            elif i == 2:
                min_rgb(nums + 1, 'B', cost + info[nums][i])

    if nums > 0 and nums < N:
        if cost >= min_cost:
            return

        elif before == 'R':
            min_rgb(nums + 1, 'G', cost + info[nums][1])
            min_rgb(nums + 1, 'B', cost + info[nums][2])

        elif before == 'G':
            min_rgb(nums + 1, 'R', cost + info[nums][0])
            min_rgb(nums + 1, 'B', cost + info[nums][2])

        else:
            min_rgb(nums + 1, 'R', cost + info[nums][0])
            min_rgb(nums + 1, 'G', cost + info[nums][1])

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# print(*info, sep= '\n')
# [26, 40, 83]
# [49, 60, 57]
# [13, 89, 99]

min_cost = 0

for i in range(N):
    min_cost += sum(info[i])

min_rgb(0, '', 0)

print(min_cost)