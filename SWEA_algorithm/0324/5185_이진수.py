import sys

sys.stdin = open('5185_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, nums = map(str, input().split())

    tmps = []
    for num in nums:
        tmps += [int(num, 16)]

    # print(tmps)
    # [4, 7, 15, 14]



    result = ''
    for tmp in tmps:
        num = ''
        for _ in range(4):
            num = str(tmp % 2) + num
            tmp = tmp // 2
        result += num

    print(f'#{tc} {result}')