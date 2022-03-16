import sys

sys.stdin = open('0214_practice1_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 행렬에 0으로 둘러주기
    nums_list = []
    nums_list = [[[0]*6] + [[0] + nums[k] for k in range(N) + [0]] + [[0]*6]]

    print(nums_list)
    # totals = 0
    # for r in range(N):
    #     total = 0
    #     up = 0
    #     right = 0
    #     down = 0
    #     left = 0
    #     for c in range(N):
    #         if r == 0:
    #             right = nums[r][c] - nums[r+1][c]
    #             if right < 0:
    #                 right = -right
    #             down = nums[r][c] - nums[r][c+1]
    #             if down =
    #
    #
    #         if c == 0:
    #
    #         else:
