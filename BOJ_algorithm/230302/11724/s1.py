import sys

sys.stdin = open('input1.txt')

N, M = map(int, input().split())

info = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
    start, end = map(int, input().split())

    info[start - 1][end - 1] = 1
    info[end - 1][start - 1] = 1

visited = [0 for _ in range(N)]

group = []

while 0 in visited:

    for i in range(N):
        if visited[i] == 0:
            group.append([i])


# print(*info, sep = '\n')
# [0, 1, 0, 0, 1, 0]
# [1, 0, 0, 0, 1, 0]
# [0, 0, 0, 1, 0, 0]
# [0, 0, 1, 0, 0, 1]
# [1, 1, 0, 0, 0, 0]
# [0, 0, 0, 1, 0, 0]