import sys

sys.stdin = open('1208_input.txt')

for tc in range(1, 11):
    # N = 덤프 횟수
    N = int(input())
    # info = 화물정보 / 얼마나 쌓여있는가
    info = list(map(int, input().split()))


    for i in range(N):
        max_height = (0, 1)
        min_height = (99, 100)
        space = 0
        for j in range(100):
            if info[j] > max_height[1]:
                max_height = (j, info[j])
            if info[j] < min_height[1]:
                min_height = (j, info[j])
        if max_height[1] - min_height[1] <= 1:
            space = max_height[1] - min_height[1]
            break
        else:
            info[max_height[0]] -= 1
            info[min_height[0]] += 1
            mx = 0
            mn = 99
            for k in range(100):
                if info[k] > mx:
                    mx = info[k]
                if info[k] < mn:
                    mn = info[k]
            space = mx - mn

    print(f'#{tc} {space}')
