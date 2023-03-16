import sys

sys.stdin = open('input2.txt')

sys.setrecursionlimit(10**9)

def check(start, end):
    global trees, max_height

    print(start, end)

    middle = (start + end) // 2

    cnt = 0

    for tree in trees:
        if tree > middle:
            cnt += tree - middle
    
    if cnt >= M:
        if middle > max_height:
            max_height = middle
            check(middle, end)
    else:
        check(start, middle)

N, M = map(int, input().split())

trees = list(map(int, input().split()))

highest = max(trees)

lowest = min(trees)

max_height = 0

check(lowest, highest)

print(max_height)

