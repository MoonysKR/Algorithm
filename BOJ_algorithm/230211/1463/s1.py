N = int(input())

def check(num, cnt):
    global min_cnt

    # print(num, cnt)
    if num == 1:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    if cnt > min_cnt:
        return

    if num % 3 == 0:
        check(num // 3, cnt + 1)

    if num % 2 == 0:
        check(num // 2, cnt + 1)
    
    check(num - 1, cnt + 1)

min_cnt = 10 ** 6

check(N, 0)

print(min_cnt)