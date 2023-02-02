# 이전 퀸들과 y 축이 다르고 x1, x2와 y1, y2의 거리차이가 같지 않으면 리스트에 추가하고 함수 재귀

import sys

sys.stdin = open('input1.txt')

from collections import deque

def get_queens(lst):
    global N, cnt

    print(lst)

    if len(lst) == N:
        cnt += 1
        return
    
    y = lst[-1][0] + 1
    
    for i in range(N):

        x = i
        flag = 0

        for j in range(len(lst)):
            if lst[j][1] == x or abs(lst[j][0] - y) == abs(lst[j][1] - x):
                flag = 1
        
        if flag == 0:
            lst.append((y, x))
            get_queens(lst)
            lst.pop()

N = int(input())

cnt = 0

lst = deque()

for i in range(N):
    lst.append((0, i))

for i in range(N):
    lst.append((0, i))
    get_queens(lst)
    lst.pop()
    print(lst)

print(cnt)