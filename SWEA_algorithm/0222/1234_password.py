import sys

sys.stdin = open('1234_password_input.txt')

for tc in range(1, 11):
    N, nums = list(map(str, input().split()))

    #
    i = 0  # 순회할 인덱스의 위치
    while len(nums) > 0 and i < len(nums) - 1:  # 숫자가 하나 이상이어야하고, nums의 마지막 두 인자를 비교해야하기 때문에 len(nums)-1보다 작아야한다.
        if nums[i] == nums[i + 1]:  # 연속으로 나온다면
            nums = nums[:i] + nums[i + 2:]  # 슬라이싱 후 연결
            i = 0  # 처음부터 재순회
        else:
            i += 1  # 아니라면 다음 탐색

    print(f'#{tc} {nums}')