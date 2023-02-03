# 이전 퀸들과 y 축이 다르고 x1, x2와 y1, y2의 거리차이가 같지 않으면 리스트에 추가하고 함수 재귀

import sys

sys.stdin = open('input1.txt')

from collections import deque

def get_queens(lst, idx):
    global N, cnt

    # print(lst)

    if idx == N:
        cnt += 1
        return 

    for i in range(N):

        flag = 0

        for j in range(idx):
            if lst[j] == i or abs(j - idx) == abs(lst[j] - i):
                flag = 1
                break
        
        if flag == 0:
            lst[idx] = i
            get_queens(lst, idx + 1)
            lst[idx] = 0

N = int(input())

cnt = 0

lst = [0 for _ in range(N)]

get_queens(lst, 0)




# for i in range(1, 16):
#     cnt = 0
#     N = i
#     lst = [0 for _ in range(N)]
#     get_queens(lst, 0)

#     print(N, cnt)