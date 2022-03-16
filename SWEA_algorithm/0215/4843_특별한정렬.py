import sys

sys.stdin = open('4843_특별한정렬_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    new_list = [0] * N
    nums = list(map(int, input().split()))

    # 오름차순 정렬
    for i in range(N-1):
        for j in range(N-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    # 짝 홀 행에 하나씩 담기
    for k in range(N):
        a = int(N-(k/2)-1)
        b = int(k-(k+1)/2)
        if k % 2 == 0:
            new_list[k] = nums[a]
        else:
            new_list[k] = nums[b]

    print(f'#{tc}', end=' ')
    print(*new_list)
