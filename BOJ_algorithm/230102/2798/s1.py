import sys 

sys.stdin = open('input2.txt')

def blackjack(lst):
    global near, nums, N, M

    if len(lst) == 3:
        sums = 0
        for i in range(len(lst)):
            sums += lst[i]
        if abs(M - near) > abs(M - sums):
            near = sums

    elif len(lst) == 0:
        for i in range(N-2):
            lst.append(nums[i])
            blackjack(lst)
            lst.pop()

    elif len(lst) == 1:
        for i in range(N-2):
            if nums[i] == lst[0]:
                tmp = i
        for j in range(tmp + 1, N - 1):
            lst.append(nums[j])
            if sum(lst) > M:
                lst.pop()
            else:
                blackjack(lst)
                lst.pop()

    elif len(lst) == 2:
        for i in range(N-1):
            if nums[i] == lst[1]:
                tmp = i
        for j in range(tmp + 1, N):
            lst.append(nums[j])
            if sum(lst) > M:
                lst.pop()
            else:
                blackjack(lst)
                lst.pop()

N , M = map(int, input().split())

nums = list(map(int, input().split()))

# print(nums)
# [5, 6, 7, 8, 9]

near = 0

blackjack([])

print(near)