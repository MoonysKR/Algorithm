import sys

sys.stdin = open('input1.txt')

from collections import deque

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

# print(*info, sep= '\n')
# [26, 40, 83]
# [49, 60, 57]
# [13, 89, 99]

min_cost = 0

for i in range(N):
    min_cost += sum(info[i])

que = deque()

que.append((0, 0, info[0][0]))
que.append((0, 1, info[0][1]))
que.append((0, 2, info[0][2]))

while que:
    print(que)

    floor, color, cost = que.popleft()

    if cost >= min_cost:
        pass

    elif floor + 1 == N:
        if cost < min_cost:
            min_cost = cost
    
    else:
        if color == 0:
            que.append((floor + 1, 1, cost + info[floor + 1][1]))
            que.append((floor + 1, 2, cost + info[floor + 1][2]))
        elif color == 1:
            que.append((floor + 1, 0, cost + info[floor + 1][0]))
            que.append((floor + 1, 2, cost + info[floor + 1][2]))
        elif color == 2:
            que.append((floor + 1, 0, cost + info[floor + 1][0]))
            que.append((floor + 1, 1, cost + info[floor + 1][1]))

print(min_cost)