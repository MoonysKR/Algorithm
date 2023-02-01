import sys

sys.stdin = open('input3.txt')

from collections import deque

R, C = map(int, input().split())

maps = [[] for _ in range(R)]

for i in range(R):
    tmp = input()
    for j in range(C):
        maps[i].append(tmp[j])

# print(*maps, sep='\n')

info = deque()

info.append((0, 0, maps[0][0]))

max_alphabets = 1

while info:
    y, x, alphabets = info.popleft()

    if len(alphabets) > max_alphabets:
        max_alphabets = len(alphabets)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]

        if new_y >= 0 and new_y <= R - 1 and new_x >= 0 and new_x <= C - 1:
            if maps[new_y][new_x] not in alphabets:
                info.append((new_y, new_x, alphabets + maps[new_y][new_x]))

print(max_alphabets)