import sys

sys.stdin = open('input2.txt')

N, M = map(int, input().split())

trees = list(map(int, input().split()))

highest = max(trees)

height = 1

flag = 0

while flag == 0:

    cnt = 0

    for tree in trees:
        if tree > highest - height:
            cnt += tree - highest + height
    
    if cnt >= M:
        flag = 1
    else:
        height += 1

print(highest - height)
