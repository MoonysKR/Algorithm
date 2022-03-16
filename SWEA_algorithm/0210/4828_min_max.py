import sys

sys.stdin = open('4828_min_max.txt')

T = int(input())

for i in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_num = nums[0]
    min_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    result = max_num - min_num

    print(f'#{i+1} {result}')
