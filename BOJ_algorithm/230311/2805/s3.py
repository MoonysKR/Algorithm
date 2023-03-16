import sys

sys.stdin = open('input2.txt')

N, M = map(int, input().split())

trees = list(map(int, input().split()))

highest = max(trees)

lowest = 1

max_height = 0

flag = 0

while flag == 0:

    middle = (lowest + highest) // 2

    cnt = 0

    for tree in trees:
        if tree > middle:
            cnt += tree - middle

    if cnt >= M:
        if middle > max_height:
            max_height = middle
            lowest = middle + 1
        else:
            flag = 1
    else:
        highest = middle -1


print(max_height)