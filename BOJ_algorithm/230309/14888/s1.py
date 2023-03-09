import sys

sys.stdin = open('input3.txt')

from collections import deque

N = int(input())

nums = list(map(int, input().split()))

pmmd = list(map(int, input().split()))

max_num = 10 ** 11 * -1
min_num = 10 ** 11

def check(lst, start, total):
    global nums, pmmd, max_num, min_num

    # print(lst, start, total)
    # print(max_num, min_num)

    if lst == [0, 0, 0, 0]:
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return
    
    if start == 0:
        check(lst, start + 1, total + nums[start])
    else:
        for i in range(4):
            if lst[i] != 0:
                if i == 0:
                    lst[0] -= 1
                    check(lst, start + 1, total + nums[start])
                    lst[0] += 1
                elif i == 1:
                    lst[1] -= 1
                    check(lst, start + 1, total - nums[start])
                    lst[1] += 1
                elif i == 2:
                    lst[2] -= 1
                    check(lst, start + 1, total * nums[start])
                    lst[2] += 1
                elif i == 3:
                    lst[3] -= 1
                    if total < 0:
                        check(lst, start + 1, -(-total // nums[start]))
                    else:
                        check(lst, start + 1, total // nums[start])
                    lst[3] += 1

check(pmmd, 0, 0)

print(max_num)
print(min_num)