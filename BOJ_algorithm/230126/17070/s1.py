import sys

sys.stdin = open('input5.txt')

N = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            maps[i][j] = 'B'

nums = [[0] * N for _ in range(N)]

# print(*maps, sep='\n')
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]

def get_ways(y, x, before):
    global N, maps, nums
    print(' ---- ')
    print(*nums, sep='\n')

    if y == 0 and x == 1:
        nums[0][1] = 1

    # 오른쪽으로 보내기
    # 1. 오른쪽이 N - 1일 경우
    # 2. 우측 다다음이 존재하고 벽이 아닐 경우
    if before == 'right' or before =='diagonal':
        if y == N - 1 and x == N - 2:
                pass
        elif x + 2 <= N - 1 and maps[y][x + 2] != 'B':
            nums[y][x + 1] += nums[y][x]
            get_ways(y, x + 1, 'right')
    
    # 아래쪽으로 보내기
    # 1. 아래쪽이 N - 1일 경우
    # 2. 하단 다다음이 존재하고 벽이 아닐 경우
    if before == 'vertical' or before =='diagonal':
        if y == N - 2 and x == N - 1:
            pass
        elif y + 2 <= N - 1 and maps[y + 2][x] != 'B':
            nums[y + 1][x] += nums[y][x]
            get_ways(y + 1, x, 'vertical')

    # 대각선으로 보내기
    if y == N - 2 and x == N - 2:
        pass
    elif y < N - 1 and x < N - 1:
        if maps[y][x + 1] != 'B' and maps[y + 1][x] != 'B' and maps[y + 1][x + 1] != 'B':
            nums[y + 1][x + 1] += nums[y][x]
            get_ways(y + 1, x + 1, 'diagonal')



get_ways(0, 1, 'right')

print(nums[N - 1][N - 1])
        