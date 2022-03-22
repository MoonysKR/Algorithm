import sys

sys.stdin = open('5097_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    nums = list(map(int,(input().split())))

    for i in range(M):
        nums.append(nums[0])
        nums = nums[1:]

    print(f'#{tc} {nums[0]}')
