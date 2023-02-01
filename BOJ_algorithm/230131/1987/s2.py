import sys

sys.stdin = open('input3.txt')

def dfs(y, x, log):
    global R, C, maps, max_alphabets

    if len(log) > max_alphabets:
        max_alphabets = len(log)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if new_y >= 0 and new_y <= R - 1 and new_x >= 0 and new_x <= C - 1:
            if maps[new_y][new_x] not in log:
                dfs(new_y, new_x, log + maps[new_y][new_x])

R, C = map(int, input().split())

maps = [[] for _ in range(R)]

for i in range(R):
    tmp = input()
    for j in range(C):
        maps[i].append(tmp[j])

max_alphabets = 1

dfs(0, 0, maps[0][0])

print(max_alphabets)