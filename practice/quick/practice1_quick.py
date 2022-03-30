import sys

sys.stdin = open('practice1_input.txt')

def quick(lst, l, r):
    pivot = lst[r]  # 기준점 == 맨 오른쪽 수
    i = l  # 왼쪽 값
    j = r  # 오른쪽 값
    while i < j:  # 왼쪽값이랑 오른쪽 값이 같아질 때까지
        while i < j and lst[i] <= pivot:  # 기준점보다 큰 값이 있으면 i 정지
            i += 1
        while i < j and lst[j] >= pivot:  # 기준점보다 작은 값이 있으면 j 정지
            j -= 1
        if i < j:  # 정지된 값이 각각 왼쪽 오른쪽에 있으면
            lst[i], lst[j] = lst[j], lst[i]  # 교체
    lst[i], lst[r] = lst[r], lst[i]  # 기준값도 가운데로 이동시켜줌
    if l < i-1:  # 좌측에 비교할게 있으면
        quick(lst, l, i-1)  # 좌측 좌우값을 인자로 함수 호출
    if i + 1 < r:  # 우측에 비교할게 있으면
        quick(lst, i + 1, r)  # 우측 좌우값을 인자로 함수 호출



T = 3

for tc in range(1, T + 1):
    nums = list(map(int, input().split(', ')))
    # print(nums)
    # [11, 45, 23, 81, 28, 34]

    l = 0

    r = len(nums) - 1

    quick(nums, l, r)

    print(*nums)
    # 11 23 28 34 45 81
    # 8 11 17 22 22 23 34 45 81 99
    # 0 0 0 0 0 1 1 1 1 1
