import sys

sys.stdin = open('input5.txt')

def min_rgb(nums, before):
    global N, info, min_cost, maps

    if nums == 0:
        for i in range(3):
            maps[nums][i] = info[nums][i]
            if i == 0:
                min_rgb(nums +1, 'R')
            elif i == 1:
                min_rgb(nums +1, 'G')
            elif i ==2:
                min_rgb(nums +1, 'B')

    elif nums > 0 and nums < N:
        if before == 'R':
            # G값 최소로 채워넣어주기
            if maps[nums][1] == 0:
                maps[nums][1] = maps[nums-1][0] + info[nums][1]
                min_rgb(nums + 1, 'G')
            elif maps[nums][1] > maps[nums-1][0] + info[nums][1]:
                maps[nums][1] = maps[nums-1][0] + info[nums][1]
                min_rgb(nums + 1, 'G')

            # B값 최소로 채워넣어주기
            if maps[nums][2] == 0:
                maps[nums][2] = maps[nums-1][0] + info[nums][2]
                min_rgb(nums + 1, 'B')
            elif maps[nums][2] > maps[nums-1][0] + info[nums][2]:
                maps[nums][2] = maps[nums-1][0] + info[nums][2]
                min_rgb(nums + 1, 'B')


        elif before == 'G':
            # R값 최소로 채워넣어주기
            if maps[nums][0] == 0:
                maps[nums][0] = maps[nums-1][1] + info[nums][0]
                min_rgb(nums + 1, 'R')
            elif maps[nums][0] > maps[nums-1][1] + info[nums][0]:
                maps[nums][0] = maps[nums-1][1] + info[nums][0]
                min_rgb(nums + 1, 'R')

            # B값 최소로 채워넣어주기
            if maps[nums][2] == 0:
                maps[nums][2] = maps[nums-1][1] + info[nums][2]
                min_rgb(nums + 1, 'B')
            elif maps[nums][2] > maps[nums-1][1] + info[nums][2]:
                maps[nums][2] = maps[nums-1][1] + info[nums][2]
                min_rgb(nums + 1, 'B')


        elif before == 'B':
            # print(*maps, sep='\n')
            # R값 최소로 채워넣어주기
            if maps[nums][0] == 0:
                maps[nums][0] = maps[nums-1][2] + info[nums][0]
                min_rgb(nums + 1, 'R')
            elif maps[nums][0] > maps[nums-1][2] + info[nums][0]:
                maps[nums][0] = maps[nums-1][2] + info[nums][0]
                min_rgb(nums + 1, 'R')

            # G값 최소로 채워넣어주기
            if maps[nums][1] == 0:
                maps[nums][1] = maps[nums-1][2] + info[nums][1]
                min_rgb(nums + 1, 'G')
            elif maps[nums][1] > maps[nums-1][2] + info[nums][1]:
                maps[nums][1] = maps[nums-1][2] + info[nums][1]
                min_rgb(nums + 1, 'G')



N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

maps = [[0] * 3 for _ in range(N)]

# print(*info, sep= '\n')
# [26, 40, 83]
# [49, 60, 57]
# [13, 89, 99]

min_cost = 0

for i in range(N):
    min_cost += sum(info[i])

min_rgb(0, '')

# print(*info, sep='\n')
# print(*maps, sep='\n')

print(min(maps[N-1]))