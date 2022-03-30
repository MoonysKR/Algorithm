import sys

sys.stdin = open('5204_input.txt')

def merge(left, right):
    global N, tmp_right, tmp_left

    result = []
    if left[-1] < right[-1]:
        tmp_left += 1
    elif left[-1] > right[-1]:
        tmp_right += 1
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result += [left[0]]
                left = left[1:]
            else:
                result += [right[0]]
                right = right[1:]
        elif len(left) > 0:
            result += [left[0]]
            left = left[1:]
        elif len(right) > 0:
            result += [right[0]]
            right = right[1:]
    # print(2, result)
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        left = []
        right = []
        mid = len(arr)//2
        for i in range(mid):
            left += [arr[i]]
        for i in range(mid, len(arr)):
            right += [arr[i]]

        # merge_sort(left)
        # merge_sort(right)
        # print(1, left)
        # print(1, right)

        return merge(merge_sort(left), merge_sort(right))



T = int(input())

for tc in range(1, T + 1):
    # N =  정수의 개수
    # arr = 숫자들
    N = int(input())
    arr = list(map(int, input().split()))

    tmp_left = 0
    tmp_right = 0

    print(f'#{tc} {merge_sort(arr)[N//2]} {tmp_right}')