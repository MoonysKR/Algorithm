import sys

sys.stdin = open('5205_input.txt')


def quick(nums, l, r):
    pivot = nums[r]
    a = l
    b = r
    while a < b:
        while nums[a] <= pivot and a < b:
            a += 1
        while nums[b] >= pivot and a < b:
            b -= 1
        if a < b:
            nums[a], nums[b] = nums[b], nums[a]
    nums[a], nums[r] = nums[r], nums[a]
    if l < a - 1:
        quick(nums, l, a - 1)
    if a + 1 < r:
        quick(nums, a + 1, r)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    quick(nums, 0, len(nums) - 1)

    print(f'#{tc} {nums[N//2]}')
