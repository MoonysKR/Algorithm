import sys

sys.stdin = open('4839_이진탐색_input.txt')

T = int(input())

for tc in range(1, T+1):
    PAB = list(map(int, input().split()))
    P = PAB[0]
    A = PAB[1]
    B = PAB[2]

    start_a = 1
    start_b = 1
    end_a = P
    end_b = P
    cnt_a = 0
    cnt_b = 0

    while start_a <= end_a:
        mid_a = (start_a + end_a) // 2
        if A == mid_a:
            cnt_a += 1
            break
        else:
            if mid_a < A:
                start_a = mid_a
                cnt_a += 1
            else:
                end_a = mid_a
                cnt_a += 1

    while start_b <= end_b:
        mid_b = (start_b + end_b) // 2
        if B == mid_b:
            cnt_b += 1
            break
        else:
            if mid_b < B:
                start_b = mid_b
                cnt_b += 1
            else:
                end_b = mid_b
                cnt_b += 1

    if cnt_a > cnt_b:
        print(f'#{tc} B')
    if cnt_a == cnt_b:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')